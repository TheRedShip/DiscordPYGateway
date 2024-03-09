from Data.DataClass import DataClass

class Client:
	def __init__(self, user_data):
		self.user_data = user_data
		for key, value in self.user_data.dict().items():
			if isinstance(value, dict):
				setattr(self, key, DataClass(value))
			else:
				setattr(self, key, value)

	