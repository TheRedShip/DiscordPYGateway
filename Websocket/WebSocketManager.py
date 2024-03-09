from constant import ALL_INTENTS, DISCORD_WS_URL,				\
					OP_IDENTIFY, OP_HELLO, OP_EVENT_DISPATCH
from Websocket.webSocketUtils import ws_heartbeat
from Utils.DataClass import DataClass
from Classes.Client import Client
from Classes.Guilds import Guilds
from threading import Thread
import websocket
import json

class WebSocketManager():
	def __init__(self, gateway, token):
		self.gateway = gateway
		self.token = token

		websocket.enableTrace(False)
		self.ws = websocket.WebSocketApp(DISCORD_WS_URL,
			on_message=self.on_message,
			on_error=self.on_error,
			on_close=self.on_close,
			on_open=self.on_open)
		
		self.events = {}
		self.on("READY", self.ready)
	
	def on_open(self, ws):
		payload = {
			"token": self.token,
			"intents": ALL_INTENTS,
			"properties": {"$os": "linux","$browser": "my_library","$device": "my_library"}
		}
		self.requests(OP_IDENTIFY, payload)

	def on_message(self, ws, data):
		data = json.loads(data)
		op = data["op"]

		if (op == OP_HELLO):
			interval = data["d"]["heartbeat_interval"]
			Thread(target=ws_heartbeat, args=(ws, interval,)).start()
		elif(op == OP_EVENT_DISPATCH):
			self.emit_events(data)

	def on_error(self, ws, error):
		print("ERROR", error)

	def on_close(self, ws, err, err_2):
		pass

	def emit_events(self, data):
		event_name = data["t"]
		event_data = data["d"]

		transformed_data = DataClass(event_data)
		if (event_name not in self.events):
			print(event_name)
		else:
			for callback in self.events[event_name]:
				callback(transformed_data)

	def on(self, event, callback):
		if (not event in self.events.keys()):
			self.events[event] = []
		self.events[event].append(callback)

	def ready(self, data):
		print("READY")
		self.gateway.client = Client(self.gateway, data.user)
		self.gateway.guilds = Guilds(self.gateway, data.guilds)
	
	def requests(self, op, d):
		payload = {
			"op": op,
			"d": d
		}
		self.ws.send(json.dumps(payload))