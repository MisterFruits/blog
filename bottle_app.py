
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, static_file

@route('/')
def hello_world():
    return 'Hello from Bottle!'

@route('/static/<filename>')
def serve_static(filename):
    return static_file(filename, root = '/home/maxiimou/prod/pythonanywhere/static')

application = default_app()

