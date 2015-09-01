# coding: utf-8
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, static_file, view, post, request

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

application = default_app()

