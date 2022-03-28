from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__, template_folder=".")
app.config["SECRET_KEY"] = "fake key man"
socketio = SocketIO(app, cors_allowed_origins="*", engineio_logger=True, logger=True)


@app.route("/")
def index():
    return render_template("index.html")

    
@socketio.on("message")
def on_message(message):
    print(f"message: {message}")
    send("Hey, from the server")

if __name__ == "__main__":
    socketio.run(app)