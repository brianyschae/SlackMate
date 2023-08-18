# socket_handler.py
import os
from slack_bolt.adapter.socket_mode import SocketModeHandler
from bot import app

# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SOCKET_TOKEN"]).start()
