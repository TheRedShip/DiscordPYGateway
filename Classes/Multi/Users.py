from Classes.Single.User import User

class Users:
	def __init__(self, gateway, users_data):
		self.users = [User(gateway, user) for user in users_data]

	def list(self):
		return self.users
	
	def get(self, id):
		for user in self.users:
			if (hasattr(user, "user_id") and user.user_id == id) or user.id == id:
				return user