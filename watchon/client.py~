import socket               # Import socket module
import os
import cv2
from socketIO_client import SocketIO, LoggingNamespace

host = '192.168.30.107' # Get local machine name
port = 8080                 # Reserve a port for your service.
statusport = 9002

statusIO = SocketIO(host, statusport, LoggingNamespace)
#s = socket.socket()
#s.connect((host, port))

def ConnectAndSend(image):
  val, buf = cv2.imencode('.bmp', image)
  print 'Connecting...'
  print 'Sending...'
  index = 0
  while (len(buf) - index > 1024):
    #print 'Sending...'
    s.send(buf[index:index+1024])
    index += 1024
  if len(buf) - index > 0:
    s.send(buf[index:len(buf)])
  s.send('\3')
  print "Done Sending"
  #s.close()                     # Close the socket when done
    
def Close():
  pass
     #s.close()

def SendStatus(name, isRover, canSee, tryingToFind, waitForResponse=False):
  print "Sending status..."
  if waitForResponse:
    statusIO.emit('status', {'canSee': canSee, 'tryingToFind': tryingToFind}, GetCmdCallback)
    statusIO.wait_for_callbacks(seconds=1)
  else:
    statusIO.emit('status', {'canSee': canSee, 'tryingToFind': tryingToFind})

def GetCmdCallback(*args):
    print "Sent status successfully."
    print('cmd was received', args)
    
if __name__ == "__main__":
  ConnectAndSend(None)
    
