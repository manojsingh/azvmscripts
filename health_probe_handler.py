# simple HTTP server which run a simple page for health probe

from bottle import route, run, redirect, response

hostname = 'localhost'
hostport = 9000
isHealthy = True  

def writebody():
    body = '<html><head><title>VM Health Check</title></head>'
    body += '<body><h2> ' + hostname + ' is Healthy </h2><ul><h3></body></html>'
    return body


@route('/')
def root():
    return writebody()


@route('/health')
def isHealthy():
    global isHealthy

    if(isHealthy):
        isHealthy = True
        return writebody()
    else:
        response.status = 404
        isHealthy = True
        return 


@route('/fail')
def fail():
    global isHealthy
    isHealthy = False
    redirect('/health')


run(host=hostname, port=hostport)
