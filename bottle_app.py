# coding: utf-8

from bottle import default_app, route, static_file, view, post, request
import datetime
import os

LONG_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
SHORT_TIME_FORMAT = '%Y-%m-%d'
ACCEPTED_EXT = (".jpg", '.jpeg', ".png")
ADVENTURE_UPLOAD_PATH = "upload/mad-dam/"

def is_regular_adventure(title, file):
    if title is None or file is None:
        return False
    _, file_ext = os.path.splitext(file.filename)
    return file_ext.lower() in ACCEPTED_EXT


@route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root = '/home/maxiimou/prod/pythonanywhere/static')

@route('/mad-dam')
@view('mad-dam')
def maddam_input():
    return dict()

@post('/mad-dam')
@view('mad-dam_submited')
def maddam_submit():
    title = request.forms.get('title')
    image = request.files.get('upload')

    if not is_regular_adventure(title, image):
        return dict(success=False)

    date = datetime.datetime.now()
    adventure_name, image_ext = os.path.splitext(image.filename)
    adventure_name = '-'.join((date.strftime(SHORT_TIME_FORMAT), adventure_name))
    adventure_dir =ADVENTURE_UPLOAD_PATH + adventure_name + '/'
    caption = request.forms.get('caption')
    if os.path.exists(adventure_dir):
        return dict(success=False)

    os.makedirs(adventure_dir)
    image.save(adventure_dir + adventure_name + image_ext)
    with open(adventure_dir + adventure_name + '.markdown', 'w') as adventure_post:
        adventure_post.write(get_adventure_config(adventure_name + image_ext, title, date, caption))

    return dict(success=True)

@view('an_adventure')
def get_adventure_config(image_name, title, date, caption=None):
    caption = caption or ''
    return dict(image_name=image_name, title=title, caption=caption, date=date.strftime(LONG_TIME_FORMAT))

application = default_app()

