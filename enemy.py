class enemy:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.width = 20
		self.height = 20
		self.health = 1

	def register_hit(self):
		self.health -= 1
		if healt == 0:
			self.die()

	def die(self):
		pass