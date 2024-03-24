from Utils.DataClass import DataClass
import time
import json

class User():
	def __init__(self, gateway, user):
		self.gateway = gateway
		self.user = user

		for key, value in self.user.items():
			if (key == "recipients" and value != []):
				for recipient_key,recipient_value in value[0].items():
					if (recipient_key == "id"):
						setattr(self, "user_id", recipient_value)
					else:
						setattr(self, recipient_key, recipient_value)
			elif isinstance(value, dict):
				setattr(self, key, DataClass(value))
			else:
				setattr(self, key, value)

	def __repr__(self):
		items = []
		for key, value in self.user.items():
			if isinstance(value, DataClass):
				items.append(f"'{key}': {value.__repr__()}")
			else:
				items.append(f"'{key}': '{value}'")
		return '{' + ', '.join(items) + '}'
	
	def send(self, message, tts=False):
		return self.gateway.client.send(self.id, message, tts)