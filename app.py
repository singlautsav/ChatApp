from flask import Flask, jsonify, request
from flask_socketio import SocketIO 


app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'ashbfjnsi7reg3487wiufd73huenvgrqiuwrhfvbwefis'
socketio = SocketIO(app)

users =[
	{'id':1,
	'name':'xyz',
	'age':40},

	{'id':2,
	'name':'az1',
	'age':21},

	{'id':3,
	'name':'xyz2',
	'age':33}
]
@app.route('/')
def index():
	return app.send_static_file('index.html')

@app.route('/users')
def getUsers():
	print("Hello")
	return jsonify(users)



@socketio.on('msg')
def handleMsg(data):
	# print(data)
	socketio.emit('push',data, broadcast = True,include_self = False)




@app.route('/users/<id>')
def getId(id):
	# result = [u for u in users if s tr(u['id'])==id]
	result = list(filter(lambda u: str(u.get('id'))==id, users))
	return jsonify(result)

# /users/sort?field=name
@app.route('/users/sort')
def getUserSorted():
	field = request.args.get('field')
	if field == 'name':
		result = sorted(users, key= lambda a:a.get('name'))
	elif field=='id':
		result = sorted(users, key = lambda a:a.get('id'))
	else:
		result = sorted(users, key = lambda a:a.get('age'))

	return jsonify(result)

def tushar():
	print('HI')
	


if __name__ == "__main__":
	socketio.run(app)