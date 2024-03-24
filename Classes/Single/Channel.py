from Utils.DataClass import DataClass
import time
import json

class Channel():
	def __init__(self, gateway, guild, channel):
		self.gateway = gateway
		self.guild = guild
		self.channel = channel

		for key, value in self.channel.items():
			if isinstance(value, dict):
				setattr(self, key, DataClass(value))
			else:
				setattr(self, key, value)

	def __repr__(self):
		items = []
		for key, value in self.channel.items():
			items.append(f"'{key}': '{value}'")
		return '{' + ', '.join(items) + '}'
	
	def send(self, message, tts=False):
		payload = {
			"content": message,
			"flags": 0,
			"mobile_network_type": "unknown",
			"nonce": str(int(time.time()*1000)),
			"tts": tts
		}
		return self.gateway.requester.post(f"channels/{self.channel.id}/messages", json.dumps(payload))