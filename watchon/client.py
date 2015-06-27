import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = 'localhost' # Get local machine name
port = 9002                 # Reserve a port for your service.

s.connect((host, port))
s.send("Hello server!")
f = open('server.js','rb')
print 'Sending...'
l = f.read(1024)
while (l):
    print 'Sending...'
    s.send(l)
    l = f.read(1024)
f.close()
print "Done Sending"
print s.recv(1024)
s.close                     # Close the socket when done
