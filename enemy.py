from random import randint
from math import sqrt, ceil

class enemy:
	def __init__(self, game):
		self.game = game
		self.x = 0
		self.y = 0
		self.random_pos()
		self.width = 20
		self.height = 20
		self.health = 1
		self.color = (0,0,255)
		self.x_vec = self.x - (game.screen_x/2)
		self.y_vec = self.y - (game.screen_y/2)
		self.correct = 1/sqrt((self.x_vec*self.x_vec)+(self.y_vec*self.y_vec))
		self.speed_x = -self.x_vec*self.correct
		self.speed_y = -self.y_vec*self.correct

	def deal_damage(self, player):
		pass

	def check_player_reachable(self, player_circle, player):
		vector = (self.x - (self.game.screen_x/2),self.y - (self.game.screen_y/2))
		if sqrt((vector[0]*vector[0])+(vector[1]*vector[1])) < (player_circle+4):
			self.speed_x = 0
			self.speed_y = 0
			self.deal_damage(player)

	def random_pos(self):
		self.x =  randint(-600,self.game.screen_x + 600)
		if self.x > self.game.screen_x+100 or self.x < -100:
			self.y =randint(-300, self.game.screen_y + 300)
		else:
			if randint(0,5000000) > 5000000/2:
				self.y = randint(self.game.screen_y + 300 , self.game.screen_y+600)
			else:
				self.y = randint(-600, -100)

	def move(self):
		self.x += self.speed_x
		self.y += self.speed_y

	def register_hit(self):
		self.health -= 1
		if self.health == 0:
			self.game.score += 1
			return True
		else:
			return False

	def die(self):
		pass