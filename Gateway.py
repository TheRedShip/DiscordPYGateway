from Websocket.WebSocketManager import WebSocketManager
import os

class Gateway():
	def __init__(self):
		self.client = None
		self.guilds = None
		self.socket = WebSocketManager(self, os.getenv("token"))

	def start(self):
		self.socket.ws.run_forever()

	def on(self, event, callback):
		self.socket.on(event, callback)