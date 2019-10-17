# workserver.py - simple HTTP server with a do_work / stop_work API
# GET /do_work activates a worker thread which uses CPU
# GET /stop_work signals worker thread to stop
import socket
import time

from bottle import route, run

hostname = socket.gethostname()
hostport = 9000
keepworking = False  # boolean to switch worker thread on or off

def writebody():
    body = '<html><head><title>VM Health Check</title></head>'
    body += '<body><h2> ' + hostname + ' is Healthy </h2><ul><h3>'
    </body></html>'
    return body


@route('/')
def root():
    return writebody()


@route('/do_work')
def do_work():
    global keepworking
    # start worker thread
    keepworking = True
    return writebody()


@route('/stop_work')
def stop_work():
    global keepworking
    # stop worker thread
    keepworking = False
    return writebody()


run(host=hostname, port=hostport)
