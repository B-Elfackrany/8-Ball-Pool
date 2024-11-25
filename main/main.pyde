# importing relevant libraries: 
import os 
import math 
import random 
add_library('sound')


# ==========================================================
# getting the current working directory: 
PATH = os.getcwd()

# ==========================================================
# declaring the constants
RESOLUTION_W = 1900
RESOLUTION_H = 1000
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
        image(table, 0, 0, RESOLUTION_W, RESOLUTION_H)
    
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
