import socket               # Import socket module
import os
import cv2
from socketIO_client import SocketIO, LoggingNamespace

host = '192.168.1.72' # Get local machine name
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

def SendWhere(name, isRover):
  print "Awaiting handshake..."
  def respond(args*):
    statusIO.emit('where', {'name': name, 'rover': isRover})
    print "Received handshake."
  statusIO.on('where', respond)
  statusIO.wait_for_callbacks(seconds=1)

def SendStatus(name, isRover, canSee, tryingToFind):
  print "Sending status..."
  statusIO.emit('status', {'canSee': canSee, 'tryingToFind': tryingToFind}, GetCmdCallback)
  statusIO.wait_for_callbacks(seconds=1)

def GetCmdCallback(*args):
    print "Sent status successfully."
    print('cmd was received', args)
    
if __name__ == "__main__":
  ConnectAndSend(None)
    
