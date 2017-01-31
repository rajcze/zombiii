from random import randint
from math import sqrt
class enemy:
	def __init__(self, x_max, y_max):
		self.x = x_max
		self.y = y_max
		self.random_pos()
		#self.center()
		self.width = 20
		self.height = 20
		self.health = 1
		self.color = (0,0,255)
		self.x_vec = self.x - (x_max/2)
		self.y_vec = self.y - (y_max/2)
		self.correct = 10/sqrt((self.x_vec*self.x_vec)+(self.y_vec*self.y_vec))
		self.speed_x = -int(self.x_vec*self.correct)
		self.speed_y = -int(self.y_vec*self.correct)

	def center(self):
		self.x /= 2 
		self.x += 20
		self.y /= 2
		self.y += 20
		self.x = int(self.x)
		self.y = int(self.y)

	def random_pos(self):
		maximum = self.x
		self.x =  randint(-600,self.x + 600)
		if self.x > maximum+100 or self.x < -100:
			self.y =randint(-300, self.y + 300)
		else:
			if randint(0,5000000) > 5000000/2:
				self.y = randint(self.y + 300 , self.y+600)
			else:
				self.y = randint(-600, -100)

	def move(self):
		self.x += self.speed_x
		self.y += self.speed_y

	def register_hit(self):
		self.health -= 1
		if healt == 0:
			self.die()

	def die(self):
		pass