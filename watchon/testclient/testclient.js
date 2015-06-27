var io = require('socket.io-client');
var port = 9002;
//var io = module.exports = sio(port);

var socket = io('http://localhost:'+port);
  socket.on('news', function (data) {
    console.log(data);
    socket.emit('my other event', { my: 'data' });
  });
