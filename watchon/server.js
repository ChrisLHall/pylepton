var sio = require('socket.io');
var port = 9002;
var io = module.exports = sio(port);
var fs = require('fs');

var sockets = [];

io.on('connection', function(socket){
  newSocket = {};
  socket.pos = sockets.length;
  newSocket.socket = socket;
  sockets.push(newSocket);

  console.log("Total connections: " + sockets.length);
  console.log('a user connected');
  socket.emit('where',{});
  socket.on('where', function(data){
    if(socket.pos == 1) {
      io.emit('target',data);
    }
    sockets[socket.pos].name = data.name;
    sockets[socket.pos].location = data.location;
    console.log(sockets);
    console.log(data);
  });
  socket.on('disconnect', function(){
    console.log('user disconnected' + socket.pos);
  });
  //socket.emit('news', { hello: 'world' });
  socket.on('my other event', function (data) {
    console.log(data);
  });

  socket.on('target',function(data) {
    console.log(data);
    io.emit('target',data);
  });


  socket.on('image', function(data) {
    time = (new Date().getTime());
    fs.writeFile('images/' + time + '-vl.jpg', data.imageVL, function(err) {
    if(err) {
        return console.log(err);
    }
    fs.writeFile('images/' + time + '-ir.jpg', data.imageIR, function(err) {
    if(err) {
        return console.log(err);
    }
  });
      fs.writeFile('images/' + (new Date().getTime()) + '-ir.jpg', data.imageIR, function(err) {
      if(err) {
          return console.log(err);
      }
});

  });

});
