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
BUFFER_SIZE = config.BUFFER_SIZE
EXT_CONFIG_PATH = config.EXT_CONFIG_PATH

# Setup the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s")

file_handler = logging.FileHandler("server.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class AS_Server:
    """A socket server that takes a string connection and searches a file to confirm if the    string exist in the file"""

    def __init__(
        self,
        host=socket.gethostbyname(socket.gethostname()),
        port=5050,
        format="utf-8",
        buffer_size=1024,
        reread_on_query=True,
    ):
        self._host = host
        self._port = port
        self._format = format
        self._reread_on_query = reread_on_query
        self._buffer_size = buffer_size
        self._running = True

    def terminate(self):
        logger.debug("[TERMINATING...]")
        self._running = False
        self._server.shutdown(socket.SHUT_RDWR)
        self._server.close()

    def _recv_data(self, conn, addr):
        pass
