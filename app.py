from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('chat message')
def handle_message(data):
    sender = data['sender']
    message = data['message']
    emit('chat message', {'sender': sender, 'message': message}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8010, debug=True, allow_unsafe_werkzeug=True )
