# importing relevant libraries: 
import os 
import math 
import random 
<<<<<<< HEAD
RATIO = 3.57
=======
add_library('sound')


>>>>>>> 727d310aa9c00961bcad96a7dba378a7ac2dddd4
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
RAIL_WIDTH = 100
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
class Point():
    def __init__(self,x,y):
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
        if self.position.y <= RAIL_WIDTH or self.position.y >= height-RAIL_WIDTH:
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
    background(256,256,256)
    image(table,0,0)
    ball.update()
    ball.display()    
    
def keyPressed():
    ball.hit(10,PI/4)
=======
RESOLUTION_W = 1000
RESOLUTION_H = 800
BALL_RADIUS = 50

# ==========================================================
# loading the media
cue = loadImage(PATH + "/media/" +"cue.png")
table = loadImage(PATH + "/media/" +"table.png")

ball_1 = loadImage(PATH + "/media/" +"ball_1.png")
ball_2 = loadImage(PATH + "/media/" +"ball_2.png")
ball_3 = loadImage(PATH + "/media/" +"ball_3.png")
ball_4 = loadImage(PATH + "/media/" +"ball_4.png")
ball_5 = loadImage(PATH + "/media/" +"ball_5.png")
ball_6 = loadImage(PATH + "/media/" +"ball_6.png")
ball_7 = loadImage(PATH + "/media/" +"ball_7.png")
ball_8 = loadImage(PATH + "/media/" +"ball_8.png")
ball_9 = loadImage(PATH + "/media/" +"ball_9.png")
ball_10 = loadImage(PATH + "/media/" +"ball_10.png")
ball_11 = loadImage(PATH + "/media/" +"ball_11.png")
ball_12 = loadImage(PATH + "/media/" +"ball_12.png")
ball_13 = loadImage(PATH + "/media/" +"ball_13.png")
ball_14 = loadImage(PATH + "/media/" +"ball_14.png")
ball_15 = loadImage(PATH + "/media/" +"ball_15.png")

collision_sound = SoundFile(this, PATH + "/media/" + "collision.mp3")
strong_collision_sound = SoundFile(this, PATH + "/media/" + "strong_collision.mp3")
pocket_sound = SoundFile(this, PATH + "/media/" + "pocket.mp3")

# ==========================================================
# classes

# Ball Class:
class Ball:
    def __init__(self, x, y, image, id, type):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.image = image
        self.rad = BALL_RADIUS
        self.type = type
    
    def display(self):
        image(self.image, self.x - BALL_RADIUS, self.y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)

# Sounds Class:
class Sound:
    def __init__(self):
        self.collision_sound = collision_sound
        self.strong_collision_sound = strong_collision_sound
        self.pocket_sound = pocket_sound
        
    def play_collision_sound(self, relative_speed):
        if relative_speed> 5: # we can change the speed value as needed
            self.strong_collision_sound.play()
        else:
            self.collision_sound.play()
    
    def play_pocket_sound(self):
        self.pocket_sound.play()
        
# Cue Class 
class Cue: 
    def __init__(self, ball):
        self.ball = ball # to keep in reference with the cue ball
        self.angle = 0 
        self.power = 0

# Game Class
class Game:
    def __init__(self):
        self.balls = []
        
    def draw(self):
        image(table, 20, 150, RESOLUTION_W - 40, RESOLUTION_H - 250)
    
    # def setup():
        #maybe we can add calls to functions to randomely generate the plases of the balls ??
        
# ==========================================================
game = Game()

def setup():
    size(RESOLUTION_W, RESOLUTION_H)
    # game.setup()
    # pocket_sound.play()  #remove this, its just for testing
    
def draw():
    background(0)
    game.draw()
>>>>>>> 727d310aa9c00961bcad96a7dba378a7ac2dddd4
