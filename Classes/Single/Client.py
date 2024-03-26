from Utils.DataClass import DataClass
import time
import json

class Client:
	def __init__(self, gateway, user_data):
		self.gateway = gateway
		self.user_data = user_data
		for key, value in self.user_data.items():
			if isinstance(value, dict):
				setattr(self, key, DataClass(value))
			else:
				setattr(self, key, value)

	def send(self, channel_id, message, tts=False):
		payload = {
			"content": message,
			"flags": 0,
			"mobile_network_type": "unknown",
			"nonce": str(int(time.time()*1000)),
			"tts": tts
		}
		return self.gateway.requester.post(f"channels/{channel_id}/messages", payload)
