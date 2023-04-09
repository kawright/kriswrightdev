"""
This top-level file contains the root of the kriswrightdev application.
"""

from bottle import default_app, route

@route('/')
def hello_world():
    return 'Hello from Bottle!'

application = default_app()

