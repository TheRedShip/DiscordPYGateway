from Classes.Single.User import User

class Users:
	def __init__(self, gateway, users_data):
		self.gateway = gateway
		self.users = [User(gateway, user) for user in users_data]

	def list(self):
		return self.users
	
	def get(self, id):
		if (id == self.gateway.client.id):
			return self.gateway.client
		for user in self.users:
			if (hasattr(user, "channel_id") and user.channel_id == id) or (hasattr(user, "id") and user.id == id):
				return user