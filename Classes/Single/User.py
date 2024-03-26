from Utils.DataClass import DataClass
import json

class User():
	def __init__(self, gateway, user):
		self.gateway = gateway
		self.user = user
	
		for key, value in self.user.items():
			if (key == "id"):
				setattr(self, "channel_id", value)
			elif (key == "recipients" and value != []):
				for recipient_key,recipient_value in value[0].items():
					setattr(self, recipient_key, recipient_value)
			elif isinstance(value, dict):
				setattr(self, key, DataClass(value))
			else:
				setattr(self, key, value)

	def __repr__(self):
		items = []
		for key, value in self.user.items():
			if (key == "id"):
				items.append(f"'channel_id': '{value}'")
			elif (key == "recipients" and value != []):
				for recipient_key,recipient_value in value[0].items():
					items.append(f"'{recipient_key}': '{recipient_value}'")
			else:
				items.append(f"'{key}': '{value}'")
		return '{' + ', '.join(items) + '}'
	
	def send(self, message, tts=False):
		return self.gateway.client.send(self.channel_id, message, tts)

	def get_dm_messages(self, limit=50, before_id=None):
		if (before_id == None):
			before_id = self.last_message_id
		payload = {
			"limit": limit,
			"before": before_id
		}
		response = self.gateway.requester.get(f"channels/{self.channel_id}/messages", payload)
		return [DataClass(msg) for msg in json.loads(response.content.decode())]