# coding: utf-8
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, static_file, view, post, request
import datetime

LONG_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
SHORT_TIME_FORMAT = '%Y-%m-%d'

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
def maddam_submit():
    title = request.forms.get('title')
    caption = request.forms.get('caption')
    image = request.files.get('upload')
    return 'Bravo ! Vous avez aidé mad-dam à faire son coup !'

@view('an_adventure')
def get_adventure_config(image_name, title, caption=None, date=None):
    date = date or datetime.datetime.now()
    caption = caption or ''
    return dict(image_name=image_name, title=title, caption=caption, date=date.strftime(LONG_TIME_FORMAT))

application = default_app()

