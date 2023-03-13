import logging
import datetime
import socket
import subprocess
import threading
import config



PORT = config.PORT
HOST = config.Host
FORMAT = config.FORMAT
REREAD_ON_QUERY = config.REREAD_ON_QUERY
BUFFER_SIZE  = config.BUFFER_SIZE
EXT_CONFIG_PATH = config.EXT_CONFIG_PATH

# Setup the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)