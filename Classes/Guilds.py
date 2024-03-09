from Classes.Guild import Guild

class Guilds:
	def __init__(self, guilds_data):
		self.guilds = [Guild(guild) for guild in guilds_data]
	
	def list(self):
		return self.guilds
	
	def get(self, id):

		for guild in self.guilds:
			if guild.id == id:
				return guild