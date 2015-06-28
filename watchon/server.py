import socket               # Import socket module
import time
import cv2

s = socket.socket()         # Create a socket object
host = '' # Get local machine name
port = 8080                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
cv2.namedWindow("Jeffery")
cv2.waitKey(1)
odd = False

c, addr = s.accept()     # Establish connection with client.
print 'Got connection from', addr
print "Receiving..."
while True:

    name = "images/" + str(time.time()) + ".bmp"

    l = c.recv(1024)
    if l:
        pass
    else:
        continue
    f = open(name,'wb')
    while (l and l[-1] != '\3'):
        #print "Receiving..."
        f.write(l)
        l = c.recv(1024)
    f.close()
    im = cv2.imread(name)
    if odd:
       odd = False
       cv2.imshow("Jeffery",im)
    else:
       odd = True
       cv2.imshow("Winston",im)
    cv2.waitKey(1)
    print "Done Receiving"
c.close()                # Close the connection
