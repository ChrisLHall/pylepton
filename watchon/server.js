var sio = require('socket.io');
var port = 9002;
var io = module.exports = sio(port);
var fs = require('fs');

io.on('connection', function(socket){
  console.log('a user connected');
  socket.on('disconnect', function(){
    console.log('user disconnected');
  });
  socket.emit('news', { hello: 'world' });
  socket.on('my other event', function (data) {
    console.log(data);
  });


  socket.on('image', function(data) {
    fs.writeFile('images/' + (new Date().getTime()) + '-vl.jpg', data.imageVL, function(err) {
    if(err) {
        return console.log(err);
    }
});

  });

});
