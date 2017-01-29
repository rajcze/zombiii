from math import sin, cos, pi

class player:
    def __init__(self):
        self.x = 1
        self.y = 1
        self.gun = 0
        self.lives = 10
        self.rotation_D = 2
        self.deg_rotation = 0
        self.rotation = self.rotation_D * (pi/180)
    def rotate_left(self):
        self.rotate(-self.rotation)

    def rotate_right(self):
        self.rotate(self.rotation)

    def rotate(self, rads):
        cosin = cos(rads)
        sinus = sin(rads)
        self.deg_rotation += (rads / (pi/180))
        self.x = cosin*self.x - sinus*self.y
        self.y = sinus*self.x + cosin*self.y
    def get_deg_rotation(self):
        return self.deg_rotation 
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_lives(self):
        return self.lives

    def get_gun(self):
        return self.gun