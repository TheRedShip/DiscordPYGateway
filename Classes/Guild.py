from Data.DataClass import DataClass

class Guild:
	def __init__(self, guild):
		self.guild = guild
		for key, value in self.guild.items():
			if isinstance(value, dict):
				setattr(self, key, DataClass(value))
			else:
				setattr(self, key, value)

	def __repr__(self):
		items = []
		for key, value in self.__dict__.items():
			if isinstance(value, DataClass):
				items.append(f"'{key}': {value.__repr__()}")
			else:
				items.append(f"'{key}': '{value}'")
		return '{' + ', '.join(items) + '}'