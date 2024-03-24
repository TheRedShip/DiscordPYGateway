from Utils.DataClass import DataClass
from Classes.Single.Member import Member
from Classes.Single.Channel import Channel

class Guild:
	def __init__(self, gateway, guild):
		self.gateway = gateway
		self.guild = guild

		for key, value in self.guild.items():
			if isinstance(value, dict):
				setattr(self, key, DataClass(value))
			elif isinstance(value, list):
				setattr(self, key, [DataClass(val) if isinstance(val, dict) else val for val in value])
			else:
				setattr(self, key, value)

	def __repr__(self):
		items = []
		for key, value in self.guild.items():
			items.append(f"'{key}': '{value}'")
		return '{' + ', '.join(items) + '}'
	
	def member(self, id):
		for member in self.members:
			if member.user.id == id:
				return Member(self.gateway, self, member)

	def channel(self, id):
		for channel in self.channels:
			if channel.id == id:
				return Channel(self.gateway, self, channel)