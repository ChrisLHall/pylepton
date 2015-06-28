import numpy as np
import cv2
from socketIO_client import SocketIO, LoggingNamespace

def SendImage(imgArray, ip):
    with SocketIO('192.168.30.46', 9002, LoggingNamespace) as socketIO:
        socketIO.emit({'imageVL': 'yyy', 'imageIR': 'jellyfish'})
        socketIO.wait(seconds=1)
