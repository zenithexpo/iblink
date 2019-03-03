
function start_python_func() {
  console.log("I've been called");
  var path = require("path")
  var python = require("python-shell")

  var options = {
    scriptPath : path.join(__dirname, '/engine/'),
  }
console.log("calling python loop")
  var instance = new python('python_loop.py', options);
  console.log("hello")

  instance.on('message', function(message) {
    if(message == "Reminder"){
      var fs = require('fs');
  		fs.readFile('config.js', 'utf8', async function(err, contents) {
      //alert(contents);
  		data=await JSON.parse(contents);
      console.log(data);
      if(data.twenty==1&&data.status==1)swal("20 Minutes Reminder, Look at a far object");
  		});
    }

  })

  instance.on('message', function(message){
    if (message == "Reminder") return;
    var notification={
      title:'Eye Blink Alert',
      body:'Your Blink last minute was: '+message,
      icon: path.join(__dirname,'icons/Hlogo.png')
    };
    var fs = require('fs');
		fs.readFile('config.js', 'utf8', function(err, contents) {
    //alert(contents);
		data=JSON.parse(contents);
    console.log(data);
    if(data.notification==1)myNotification = new window.Notification(notification.title, notification);
		});

  })
}
