# coding: utf-8

from bottle import default_app, route, static_file, view, post, request
import datetime
import os

LONG_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
SHORT_TIME_FORMAT = '%Y-%m-%d'
ACCEPTED_EXT = (".jpg", '.jpeg', ".png")

def is_regular_adventure(title, file_ext):
    if title == '':
        return False
    return file_ext.lower() in ACCEPTED_EXT


@route('/')
def hello_world():
    return 'Hello from Bottle!'

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
    title = request.forms.get('title') or ''
    image = request.files.get('upload') or ''

    adventure_name, file_ext = os.path.splitext(image.filename)
    if not is_regular_adventure(title, file_ext):
        return dict(success=False)

    caption = request.forms.get('caption') or None
    date = datetime.datetime.now()

    adventure_name = '-'.join((date.strftime(SHORT_TIME_FORMAT), adventure_name))
    return dict(success=True)

@view('an_adventure')
def get_adventure_config(image_name, title, caption=None, date=None):
    date = date or datetime.datetime.now()
    caption = caption or ''
    return dict(image_name=image_name, title=title, caption=caption, date=date.strftime(LONG_TIME_FORMAT))

application = default_app()

