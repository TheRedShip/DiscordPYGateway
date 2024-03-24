from Websocket.WebSocketManager import WebSocketManager
from Utils.Requester import Requester

class Gateway():
	def __init__(self, token):
		self.client = None
		self.guilds = None
		self.users = None
		self.requester = Requester(token)
		self.socket = WebSocketManager(self, token)

	def start(self):
		self.socket.ws.run_forever()

	def on(self, event, callback):
		self.socket.on(event, callback)