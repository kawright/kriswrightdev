"""
This top-level file contains the root of the kriswrightdev application.
"""

from bottle import default_app, route, run

@route('/')
def hello_world():
    return 'Hello from Bottle!'

application = default_app()

if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)
