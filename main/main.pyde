# importing relevant libraries: 
import os 
import math 
import random 
<<<<<<< HEAD
RATIO = 3.57
# ==========================================================
# getting the current working directory: 
PATH = os.getcwd()

# ==========================================================
# declaring the constants
<<<<<<< HEAD
RESOLUTION_W = 1275
RESOLUTION_H = 720
BALL_TYPES = ["cue","solid","solid","solid","solid","solid","solid","solid","8-ball","stripes","stripes","stripes","stripes","stripes","stripes","stripes"]
FRICTION = 0.03
BALL_RADIUS = 20
RAIL_WIDTH = 50
# ==========================================================
# loading the images
cue = loadImage(PATH + "/assets/" +"cue.png")
table = loadImage(PATH+"/media/" + "table.png")
ball_1 = loadImage(PATH + "/media/" +"ball_1.png")
ball_2 = loadImage(PATH + "/assets/" +"ball_2.png")
ball_3 = loadImage(PATH + "/assets/" +"ball_3.png")
ball_4 = loadImage(PATH + "/assets/" +"ball_4.png")
ball_5 = loadImage(PATH + "/assets/" +"ball_5.png")
ball_6 = loadImage(PATH + "/assets/" +"ball_6.png")
ball_7 = loadImage(PATH + "/assets/" +"ball_7.png")
ball_8 = loadImage(PATH + "/assets/" +"ball_8.png")
ball_9 = loadImage(PATH + "/assets/" +"ball_9.png")
ball_10 = loadImage(PATH + "/assets/" +"ball_10.png")
ball_11 = loadImage(PATH + "/assets/" +"ball_11.png")
ball_12 = loadImage(PATH + "/assets/" +"ball_12.png")
ball_13 = loadImage(PATH + "/assets/" +"ball_13.png")
ball_14 = loadImage(PATH + "/assets/" +"ball_14.png")
ball_15 = loadImage(PATH + "/assets/" +"ball_15.png")

# ==========================================================
# classes

# Ball Class:
class Ball:
    def __init__(self, x, y, image, id, type):
        self.x = x
        self.y = y
    def set(self,other):
        if isinstance(other,Point):
            self.x = other.x
            self.y = other.y
        else:
            self.x = other[0]
            self.y = other[1]
    def move(self,other):
        if isinstance(other,Point):
            self.x += other.x
            self.y +=other.y
        else:
            self.x += other[0]
            self.y += other[1]
        
class Ball():
    def __init__(self,x,y,ID):
        self.ID = ID
        self.radius = BALL_RADIUS
        self.type = BALL_TYPES[self.ID]
        self.img = loadImage(PATH + "/media/" +"ball_"+str(ID)+".png")
        self.img.resize(int(self.img.width//RATIO),int(self.img.height//RATIO))
        self.position = Point(x,y)
        self.velocity = Point(0,0)
        self.friction = FRICTION 
    def hit(self,power, angle):
        x_comp = power * cos(angle)
        y_comp = power * sin(angle)
        print(x_comp,y_comp)
        self.velocity.move([x_comp,y_comp])
    def apply_friction(self):
        v = math.sqrt(self.velocity.x**2 + self.velocity.y**2)
        friction_x = FRICTION*v
        friction_y = FRICTION*v if v != 0 else 0
        self.velocity.set([max(0,abs(self.velocity.x)-FRICTION)*(-1 if self.velocity.x<0 else 1),
                          max(0,abs(self.velocity.y)-FRICTION)*(-1 if self.velocity.y<0 else 1)])
    def check_collision(self):
        if self.position.x <= RAIL_WIDTH or self.position.x >= width-RAIL_WIDTH:
            self.velocity.x*=-1
        if self.position.y-self.radius <= RAIL_WIDTH or self.position.y+self.radius >= height-RAIL_WIDTH:
            self.velocity.y*=-1
    def update(self):
        self.position.move(self.velocity)
        self.apply_friction()
        self.check_collision()
        
    def display(self):
        image(self.img,self.position.x,self.position.y)

def setup():
    size(RESOLUTION_W, RESOLUTION_H)
    background(256,256,256)
    table.resize(int(table.width//RATIO),int(table.height//RATIO))
    # ball_1.resize(int(ball_1.width//RATIO),int(ball_1.height//RATIO))
ball = Ball(100,100,1)
def draw():
    background(0)
    game.draw()
