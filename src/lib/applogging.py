import logging
import cherrypy
from queuelogginghandler import QueueLoggingHandler

def setup_logging():
    '''Set up a QueueLoggingHandler'''
    log = cherrypy.log
    
    # Remove the default FileHandlers if present.
    log.error_file = ""
    log.access_file = ""
    
    queueHandler = QueueLoggingHandler()
    queueHandler.setLevel(logging.DEBUG)
    log.error_log.addHandler(queueHandler)