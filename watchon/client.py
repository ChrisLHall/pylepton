import socket               # Import socket module
import os
import cv2

host = '192.168.1.72' # Get local machine name
port = 8080                 # Reserve a port for your service.
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
    
if __name__ == "__main__":
  ConnectAndSend(None)
    
