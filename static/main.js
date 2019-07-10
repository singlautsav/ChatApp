var socket = io.connect(location.protocol +'//'+ document.domain+ ':'+location.port)

function send(){
	var msgBox = document.getElementById('msgBox')
	socket.emit('msg',msgBox.value)
	msgBox.value = ""
}	 

// source venv\Lib\activate
socket.on('push', function(data){
	var msgList = document.getElementById('msgList')
	msgList.innerHTML += "<p>"+data+"</p>"
// console.log(data)
})