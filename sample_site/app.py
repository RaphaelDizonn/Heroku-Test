from flask import Flask, render_template
from flask_socketio import SocketIO, send



app = Flask(__name__)
app.config['SECRET_KEY'] = '39ccdde2930edbf62e9efcb5bc318da5dc8b58d9978de52c3d43cda83fbd3a49'


socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/') 
def home():
 return render_template('index.html')

@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + msg)
	send(msg, broadcast=True)




if __name__ == '__main__':
	socketio.run(app)

