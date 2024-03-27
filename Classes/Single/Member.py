from Utils.DataClass import DataClass

class Member():
	def __init__(self, gateway, guild, member):
		self.gateway = gateway
		self.guild = guild
		self.member = member

		for key, value in self.member.items():
			if isinstance(value, dict):
				setattr(self, key, DataClass(value))
			else:
				setattr(self, key, value)

	def __repr__(self):
		items = []
		for key, value in self.member.items():
			items.append(f"'{key}': '{value}'")
		return '{' + ', '.join(items) + '}'
	
	def send(self, message, tts=False):
		private_channel_id = self.gateway.users.get(self.id).channel_id
		return self.gateway.client.send(private_channel_id, message, tts)