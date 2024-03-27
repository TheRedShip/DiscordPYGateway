

class DataClass:
	def __init__(self, data):
		if (isinstance(data, list)):
			data = data[0]
		for key, value in data.items():
			if isinstance(value, dict):
				setattr(self, key, DataClass(value))
			else:
				setattr(self, key, value)

	def __repr__(self):
		items = []
		for key, value in self.__dict__.items():
			if (isinstance(value, str)):
				items.append(f"'{key}': '{value}'")
			else:
				items.append(f"'{key}': {value}")
		return '{' + ', '.join(items) + '}'
	
	def has(self, param):
		return hasattr(self, param)

	def items(self):
		return self.__dict__.items()
	
	def dict(self):
		return self.__dict__

