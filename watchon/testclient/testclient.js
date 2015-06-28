var io = require('socket.io-client');
var port = 9002;
//var io = module.exports = sio(port);

var socket = io('http://localhost:'+port);
  socket.on('news', function (data) {
    console.log(data);
    socket.emit('image', { imageVL: 'data' });
  });
  socket.on('where', function(data) {
    console.log(data);
    socket.emit('where', {name:process.argv[2],location:process.argv[3]})
  });
  socket.on('target', function(data) {
    console.log(data);
    //socket.emit('', {name:'batman'})
  });
