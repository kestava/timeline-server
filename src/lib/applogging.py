import logging
import cherrypy
from queuelogginghandler import QueueLoggingHandler

def setup_logging():
    '''Set up a QueueLoggingHandler'''
    logger = cherrypy.log
    
    # Remove the default FileHandlers if present.
    logger.error_file = ""
    logger.access_file = ""
    
    logger = logging.getLogger('app')
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    
    queueHandler = QueueLoggingHandler()
    logger.addHandler(queueHandler)