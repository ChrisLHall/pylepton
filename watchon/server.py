import socket               # Import socket module
import time

s = socket.socket()         # Create a socket object
host = 'localhost' # Get local machine name
port = 9002                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
f = open("images/" + str(time.time()) + ".jpg",'wb')
s.listen(5)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    print "Receiving..."
    l = c.recv(1024)
    while (l):
        print "Receiving..."
        f.write(l)
        l = c.recv(1024)
    f.close()
    print "Done Receiving"
    c.send('Thank you for connecting')
    c.close()                # Close the connection
