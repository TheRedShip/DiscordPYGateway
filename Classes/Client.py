from Utils.DataClass import DataClass

class Client:
	def __init__(self, gateway, user_data):
		self.gateway = gateway
		self.user_data = user_data
		for key, value in self.user_data.items():
			if isinstance(value, dict):
				setattr(self, key, DataClass(value))
			else:
				setattr(self, key, value)

	