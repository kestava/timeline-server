"""
Timeline server

Serves near real-time timeline data to web clients who connect using Comet
"long polling" methods
"""

def app(environ, start_response):
    """Simplest possible application object"""
    
    data = 'Hello, World!\n'
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain'),
        ('Content-Length', str(len(data)))
    ]
    
    start_response(status, response_headers)
    return iter([data])