

class DataClass:
	def __init__(self, data):
		for key, value in data.items():
			if isinstance(value, dict):
				setattr(self, key, DataClass(value))
			else:
				setattr(self, key, value)
	
	def __repr__(self):
		items = []
		for key, value in self.__dict__.items():
			items.append(f"'{key}': '{value}'")
		return '{' + ', '.join(items) + '}'
	
	def items(self):
		return self.__dict__.items()
	
	def dict(self):
		return self.__dict__

