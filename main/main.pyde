# importing relevant libraries: 
import os 
import math 
import random 

# ==========================================================
# getting the current working directory: 
PATH = os.getcwd()

# ==========================================================
# declaring the constants
RESOLUTION_W = 1900
RESOLUTION_H = 1000
BALL_RADIUS = 50

# ==========================================================
# loading the images
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
    def __init__(self, path):
        self.path = path 
        self.loops = 1
        
# Cue Class 
class Cue: 
    def __init__(self, ball):
        self.ball = ball # to keep in reference with the cue ball
        self.angle = 0 
        self.power = 0

class Game:
    
# ==========================================================

def setup():
    size(RESOLUTION_W, RESOLUTION_H)
    image(table, 0, 0, RESOLUTION_W, RESOLUTION_H)
