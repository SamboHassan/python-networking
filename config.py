import socket

PATH = "./data/200k.txt"
BUFFER_SIZE = 4096
EXT_CONFIG_PATH = "./ext_config.txt"
Host = socket.gethostbyname(socket.gethostname)
PORT = 5055
FORMAT = "utf-8"
REREAD_ON_QUERY = True
DISCONNECT_MESSAGE = "!DISCONNECT"