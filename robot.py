from World import *
from math import cos
from math import sin
from math import radians

class Robot():
    def __init__(self,x,y,theta):
        self.x = x
        self.y = y
        self.theta = radians(theta)
        self.new_x = x
        self.new_y = y


    def draw_robot(self):
        pygame.draw.circle(screen,(0,0,0),(self.x ,self.y),22,0)
        pygame.draw.circle(screen,(0,0,200),(self.x ,self.y),20,0)
        x_theta = cos(self.theta)*20
        y_theta = sin(self.theta)*20
        pygame.draw.line(screen,(0,0,0),(self.x ,self.y),(x_theta+self.x ,y_theta+self.y),3)
        font = pygame.font.Font(None, 20)
        text = font.render("B1", 1, (10, 10, 10))
        textpos = (self.x - 5, self.y - 40)
        screen.blit(text, textpos)


    def motion_model(self,front,rotate):
        self.new_x += cos(radians(rotate))*front
        self.new_y += sin(radians(rotate))*front

        self.x = int(self.new_x)
        self.y = int(self.new_y)

        if self.x > 1040:
           self.x = 1040
        elif self.x < 0:
            self.x = 0

        if self.y > 740:
            self.y = 740
        elif self.y < 0:
            self.y = 0

        self.theta = radians(rotate)
        self.draw_robot()