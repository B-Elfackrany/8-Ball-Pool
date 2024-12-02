# importing relevant libraries: 
import os 
import math 
import random 
# add_library('sound')
# add_library('gifAnimation')

# ==========================================================
# dimensions 
# width of game = 1000
# height of game = 800
# coordinates of top left corner of pool table image: (20, 150)
# center of pocket 1 = (65, 201, 45, 45)
# center of pocket 2 = (495, 190, 40, 40)
# center of pocket 3 = (928, 201, 45, 45)
# center of pocket 4 = (65, 650, 45, 45)
# center of pocket 5 = (495, 660, 40, 40)
# center of pocket 6 = (928, 650, 45, 45)
# top cushion 1 line(110, 213, 462, 213)
# top cushion 2 line(525, 213, 884, 213)
# bottom cushion 1 line(110, 635, 462, 635)
# bottom cushion 2 line(525, 635, 884, 635)
# verticle cushion 1 line(82, 246, 82, 602)
# verticle cushion 2 line(917, 246, 917, 602)

# ==========================================================
# getting the current working directory: 
PATH = os.getcwd()

# ==========================================================
# declaring the constants
UPPER_RAIL = 213
BOTTOM_RAIL = 635
LEFT_RAIL = 82
RIGHT_RAIL = 917
RESOLUTION_W = 1000
RESOLUTION_H = 800
BALL_RADIUS = 15
BALL_TYPES = ["cue","solid","solid","solid","solid","solid","solid","solid","8-ball","stripes","stripes","stripes","stripes","stripes","stripes","stripes"]
FRICTION = 0.2

# ==========================================================
# loading the media
cue = loadImage(PATH + "/media/" +"ball_0.png")
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

avatar1 = loadImage(PATH + "/media/" +"avatar1.png")
avatar2 = loadImage(PATH + "/media/" +"avatar2.png")

# bgGIF = Gif(this, PATH + "/media/" + "bg_gif.gif")

collision_sound = SoundFile(this, PATH + "/media/" + "collision.mp3")
strong_collision_sound = SoundFile(this, PATH + "/media/" + "strong_collision.mp3")
pocket_sound = SoundFile(this, PATH + "/media/" + "pocket.mp3")
mario_sound = SoundFile(this, PATH + "/media/" + "mariokart.mp3")

# font = loadFont(PATH + "/media/" +"font.ttf")

play_button = loadImage(PATH + "/media/" + "play_button.png")
help_button = loadImage(PATH + "/media/" + "help_button.png")
quit_button = loadImage(PATH + "/media/" + "quit_button.png")
sound_button = loadImage(PATH + "/media/" + "sound_button.png")
home_page_image = loadImage(PATH + "/media/" + "home_page.PNG")

# ==========================================================
# classes
# Sounds Class:
# class Sound:
#     def __init__(self):
#         self.collision_sound = collision_sound
#         self.strong_collision_sound = strong_collision_sound
#         self.pocket_sound = pocket_sound
#         self.mario_sound = mario_sound
#         self.is_sound_on = True
#         self.volume_level = 1.0
#         self.is_decreasing = True
        
#     def play_collision_sound(self, relative_speed):
#         #this functions plays the collision sound when balls collide
#         if relative_speed> 5: # we can change the speed value as needed
#             self.strong_collision_sound.play()
#         else:
#             self.collision_sound.play()
    
#     def play_pocket_sound(self):
#         # this function plays the pocket sound when a ball is pocketed
#         self.pocket_sound.play()
    
#     def play_mario_sound(self):
#         # this function plays the background music 
#         self.mario_sound.play()
#         self.mario_sound.loop()
#         self.mario_sound.amp(self.volume_level)
        
#     def toggle_sound(self):
#         if not self.is_sound_on:            
#             self.mario_sound.loop()
#             self.is_sound_on = True             
#         else:
#             if self.is_decreasing:
#                 # Decrease volume if sound is on
#                 self.volume_level = max(0.0, self.volume_level - 0.1)  # Cap volume at 0.0
#                 if self.volume_level == 0.0:
#                     self.is_decreasing = False
#             else:
#                 self.volume_level = min(1.0, self.volume_level + 0.1)
#                 if self.volume_level == 1.0:
#                     self.is_decreasing = True       

#             self.mario_sound.amp(self.volume_level)
        
#Point Class:
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
            
# Ball Class:
class Ball:
    def __init__(self,x,y,ID):
        self.ID = ID
        self.radius = BALL_RADIUS
        self.type = BALL_TYPES[self.ID]
        self.img = loadImage(PATH + "/media/" +"ball_"+str(ID)+".png")
        # self.img.resize(BALL_RADIUS*2,BALL_RADIUS*2)
        self.position = Point(x,y)
        self.velocity = Point(0,0)
        self.friction = FRICTION 
        self.is_pocketed = 0
        
        self.is_pocketed = 0
    def hit(self,power, angle):
        print('hit')
        x_comp = power * cos(angle)
        y_comp = power * sin(angle)
        # print(x_comp,y_comp)
        self.velocity.move([x_comp,y_comp])
    
    def pocket(self):
        print('pocketed')
        self.is_pocketed=1    
    def apply_friction(self):
        v = math.sqrt(self.velocity.x**2 + self.velocity.y**2)
        if v == 0:
            return
        theta = acos(abs(self.velocity.x)/v) if v!=0 else 0
        v = max(0,v-FRICTION)
        self.velocity.x = v*cos(theta)*(-1 if self.velocity.x<0 else 1)
        self.velocity.y = v*sin(theta)*(-1 if self.velocity.y<0 else 1)
    def collide(self, other):
        dx = self.position.x - other.position.x
        dy = self.position.y - other.position.y
        distance = math.sqrt(dx**2 + dy**2)
        nx = dx / distance
        ny = dy / distance
        dvx = self.velocity.x - other.velocity.x
        dvy = self.velocity.y - other.velocity.y
        dot_product = dvx * nx + dvy * ny
        if dot_product > 0:
            return
        impulse = 2 * dot_product / (1 + 1)
        self.velocity.x -= impulse * nx
        self.velocity.y -= impulse * ny
        other.velocity.x += impulse * nx
        other.velocity.y += impulse * ny
        
        overlap = self.radius + other.radius - distance
        self.position.x += overlap * nx / 2
        self.position.y += overlap * ny / 2
        other.position.x -= overlap * nx / 2
        other.position.y -= overlap * ny / 2

    def check_collision(self):

        if self.position.x-self.radius <= LEFT_RAIL:
            if(self.position.y-self.radius>=245 and self.position.y+self.radius<=602):
                self.position.x = LEFT_RAIL+self.radius
                self.velocity.x*=-1
            else:
                self.pocket()
        elif self.position.x+self.radius >= RIGHT_RAIL:
            if (self.position.y-self.radius>=245 and self.position.y+self.radius<=602):
                self.position.x = RIGHT_RAIL-self.radius
                self.velocity.x*=-1
            else:
                self.pocket()
        if self.position.y-self.radius <= UPPER_RAIL:
            if(462+self.radius>=self.position.x>=110-self.radius  or 884+self.radius>=self.position.x>=525-self.radius):
                self.position.y = UPPER_RAIL+self.radius
                self.velocity.y*=-1
            else:
                self.pocket()
        elif self.position.y+self.radius >= BOTTOM_RAIL:
            if (462+self.radius>=self.position.x>=110-self.radius  or 884+self.radius>=self.position.x>=525-self.radius):
                self.position.y = BOTTOM_RAIL-self.radius
                self.velocity.y*=-1
            else:
                self.pocket()
    def update(self):
        if not self.is_pocketed:
            # print(self.ID)
            self.position.move(self.velocity)
            self.apply_friction()
            self.check_collision()
        
    def display(self):
        if self.ID==0:
            print("I AM HERE MFERS")
        if not self.is_pocketed:
            imageMode(CENTER)
            image(self.img,self.position.x,self.position.y)
            imageMode(CORNER)

class CueBall(Ball):
    def __init__(self,x,y,ID):
        Ball.__init__(self,x,y,ID)
        
    def track(self):
        x,y=mouseX-self.position.x,mouseY-self.position.y
        angle = math.atan(float(y) / (x)) if x!=0 else PI/2
        if(x>0 and y<0):
            angle = PI+angle
        elif (x>=0 and y>=0):
            angle = PI+angle
        elif (x<0 and y>0):
            angle = 2*PI+angle
        
        tracker = Point(100*-cos(angle)+self.position.x,100*-sin(angle)+self.position.y)
        # print(tracker.x,tracker.y)
        if(self.velocity.x==0 and self.velocity.y==0):
            fill(255,0,0)
            circle(tracker.x,tracker.y,5)
            stroke(3)
            # strokeFill(220, 220, 220)
            line(100*cos(angle)+self.position.x,100*sin(angle)+self.position.y,200*cos(angle)+self.position.x,200*sin(angle)+self.position.y)
        return angle
        
    # def update(self):
    #     self.track()

# Game Class
class Game:
    def __init__(self):
        self.alive=0
        self.balls = []
        self.balls.append(Ball(240+30,275+150,1))
        self.balls.append(Ball(210+30,260+150,2))
        self.balls.append(Ball(210+30,290+150,3))
        self.balls.append(Ball(180+30,245+150,4))
        self.balls.append(Ball(180+30,305+150,15))
        self.balls.append(Ball(150+30,230+150,5))
        self.balls.append(Ball(150+30,260+150,6))
        self.balls.append(Ball(150+30,290+150,7))
        self.balls.append(Ball(180+30,275+150,8))
        self.balls.append(Ball(150+30,320+150,9))
        self.balls.append(Ball(120+30,215+150,10))
        self.balls.append(Ball(120+30,245+150,11))
        self.balls.append(Ball(120+30,275+150,12))
        # self.balls.append(Ball(120+30,305+150,13))
        self.balls.append(Ball(120+30,335+150,14))

        self.cue = CueBall(200,600,0)
        # seballs.append(cue)
        self.pockets =[]

        self.curx=0
        self.cury=0
    def start(self):
        print("I AM ALIVE")
        self.alive=1
    def drag(self,x,y):
        if self.alive:
            self.curx=x
            self.cury=y
    def hit(self,x,y):
        if self.alive and (self.curx !=0 or self.cury!=0):
            distance = math.sqrt((x-self.curx)**2+(y-self.cury)**2)
            angle = self.cue.track()
            print('aaa')
            print(distance,angle)
            self.cue.hit(distance/15,angle)
        
    def draw_avatars_and_names(self):
        image(avatar1, RESOLUTION_W/2 - 150, 20, 100, 100)
        image(avatar2, RESOLUTION_W/2 + 50, 20, 100, 100)
        
        fill(255,255,255)
        textSize(20)
        textAlign(CENTER)
        text("Player 1", RESOLUTION_W/2 - 200, 50)
        text("Player 2", RESOLUTION_W/2 + 200, 50)
        
    def drawBallPlaceholders(self):
        positions = [(200, 50), (230, 50), (260, 50), (290, 50), (320, 50), 
                     (350, 50), (380, 50), (410, 50), (440, 50), (470, 50), 
                     (500, 50), (530, 50), (560, 50), (590, 50), (620, 50)]
        noStroke()
        for x, y in positions:
            fill(255,255,255) 
            # ellipse(x, y, 30, 30)
    
    # def setup():
        #maybe we can add calls to functions to randomely generate the plases of the balls ??
    def check_collision(self,ball1,ball2):
        distance = math.sqrt((ball1.position.x-ball2.position.x)**2+(ball1.position.y-ball2.position.y)**2)
        if distance<=2*BALL_RADIUS:
            ball1.collide(ball2)
    def update(self):
        for ball in self.balls:
            ball.update()
        print("UPDATING GAME")
        self.cue.update()
        for ball1 in self.balls:
            for ball2 in self.balls:
                if (ball1.ID == ball2.ID):
                    continue
                self.check_collision(ball1,ball2)
            self.check_collision(ball1,self.cue)
        
    def draw_avatars_and_names(self):
        image(avatar1, RESOLUTION_W/2 - 150, 20, 100, 100)
        image(avatar2, RESOLUTION_W/2 + 50, 20, 100, 100)
        
        fill(0,0,0)
        textSize(20)
        # textFont(font)
        textAlign(CENTER)
        text("Player 1", RESOLUTION_W/2 - 200, 50)
        text("Player 2", RESOLUTION_W/2 + 200, 50)
        
    def drawBallPlaceholders(self):
        # this function makes the placeholders for the balls of each player
        positions = [(RESOLUTION_W/2 -410, 100), (RESOLUTION_W/2 -370, 100), 
                     (RESOLUTION_W/2 -330, 100), (RESOLUTION_W/2 -290, 100), 
                     (RESOLUTION_W/2 -250, 100), (RESOLUTION_W/2 - 210, 100), 
                     (RESOLUTION_W/2 -170 , 100), (RESOLUTION_W/2 + 170, 100), 
                     (RESOLUTION_W/2 + 210, 100), (RESOLUTION_W/2 +250, 100), 
                      (RESOLUTION_W/2 +290, 100), (RESOLUTION_W/2 +330, 100), 
                      (RESOLUTION_W/2 +370, 100), (RESOLUTION_W/2 +410, 100)]
        noStroke()
        for x, y in positions:
            fill(0,0,0) 
            ellipse(x, y, 30, 30)
            
    def pick_starting_player(players):
        starting_player = random.choice(players)
        # print(starting_player.name + "is starting the game and gets to break.")
        return starting_player

    def assign_groups_on_first_pocket(self, ball, current_player, opponent):
        if not current_player.group and ball.type in ["solids", "stripes"]:
            current_player.assign_group(ball.type)
            opponent.assign_group("solids" if ball.type == "stripes" else "stripes")
            
    def draw(self):

        if self.alive:
            print("TESTTT")
            image(table, 20, 150, RESOLUTION_W - 40, RESOLUTION_H - 250)
            self.cue.track()
            self.update()
            print(self.cue.velocity.x,self.cue.velocity.y)
            for ball in self.balls:
                ball.display()
            self.cue.display()
            self.draw_avatars_and_names()
            self.drawBallPlaceholders()

    def setup(self):
        player1 = Player("Player 1")
        player2 = Player("Player 2")
        players = [player1, player2]
        current_player = pick_starting_player(players)

# Player class 
class Player:
    def __init__(self, name):
        self.name = name 
        self.group = None
        self.list_of_balls = []
        
    def assign_group(self, group):
        self.group = group

class Button:
    def __init__(self, x, y, w, h, image, action):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = image
        self.action = action
    
    def display(self):
        image(self.image, self.x, self.y, self.w, self.h)
    
    def is_hovered(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x + self.w and self.y <= mouse_y <= self.y + self.h
    
    def handle_click(self):
        if self.action:
            self.action()

# Functions used in the homepage class
def start_game():
    global homepage
    homepage.on_home_page = False
    game.start()
   
def draw_game():
    background(255, 255, 255)
    game.draw()

def quit_game():
    exit()

def toggle_sound():
    print("Toggling sound")
    sound_manager.toggle_sound()
    
# Homepage class
class HomePage:
    def __init__(self):
        self.buttons = []
        self.home_page_image = home_page_image
        self.on_home_page = True
        self.on_instructions_page = False
        self.setup_buttons()
        
    def setup_buttons(self):
        self.buttons.append(Button(350, 300, 320, 110, play_button, start_game))
        self.buttons.append(Button(450, 400, 100, 100, help_button, self.show_instructions))
        self.buttons.append(Button(450, 500, 100, 100, sound_button, toggle_sound))
        self.buttons.append(Button(350, 600, 320, 110, quit_button, quit_game))

    def draw_home_page(self):
        background(0)
        image(self.home_page_image, 0, 0, RESOLUTION_W, RESOLUTION_H, 211, 0, 1498, 1080)
        for button in self.buttons:
            button.display()

    def draw_instructions_page(self):
        background(150, 123, 182)
        textAlign(CENTER, CENTER)
        textSize(15)
        fill(255)
        rules = """RULES OF 8-BALL POOL
Objective:
Be the first to pocket all your group of balls (solids or stripes) and then legally pocket the 8-ball.

Setup:
One player breaks (hits the triangle to start the game).

Gameplay:
- After the break, the table is "open" (no group assigned yet).
- The group (solids or stripes) is assigned when a player legally pockets a ball.

Taking Turns:
- You continue your turn as long as you legally pocket a ball from your group.
- If you miss or commit a foul, your opponent takes their turn.

Legal Shots:
- Always hit your group of balls first (solids or stripes).
- After hitting your ball, any ball must touch a rail or be pocketed.

The 8-Ball:
- Can only be hit after all your group balls are pocketed.
- Must call the pocket for the 8-ball before shooting.

Fouls:
- Failing to hit your group ball first, failing to hit a rail or pocket a ball after contact, pocketing the cue ball.
Fouls give the opponent ball in hand, allowing them to place the cue ball anywhere.

Winning:
You win by legally pocketing the 8-ball after clearing your group balls.

Losing:
- You pocket the 8-ball before clearing your group balls or you pocket the cue ball while pocketing the 8-ball.
"""
        text(rules, RESOLUTION_W / 2, RESOLUTION_H / 2)

        fill(0, 0, 0)
        rect(20, 10, 100, 50, 10)
        fill(255)
        textSize(20)
        text("BACK", 70, 32)

    def handle_mouse_press(self, mouse_x, mouse_y):
        if self.on_home_page:
            for button in self.buttons:
                if button.is_hovered(mouse_x, mouse_y):
                    button.handle_click()
        elif self.on_instructions_page:
            # Check if the Back button is clicked
            if 20 <= mouse_x <= 120 and 10 <= mouse_y <= 60:
                self.on_instructions_page = False
                self.on_home_page = True

    def show_instructions(self):
        self.on_home_page = False
        self.on_instructions_page = True
                
# ==========================================================

game = Game()
# player = Player()
homepage = HomePage()
# sound_manager = Sound()

def setup():
    size(RESOLUTION_W, RESOLUTION_H)
    # sound_manager.play_mario_sound()
    # game.setup()
    # pocket_sound.play()  #remove this, its just for testing
    # mario_sound.play() 
    # mario_sound.loop()
    
def mouseReleased():
    game.hit(mouseX,mouseY)
    
    
def draw():
    global homepage
    if homepage.on_home_page:
        homepage.draw_home_page()
    elif homepage.on_instructions_page:
        homepage.draw_instructions_page()
    elif not game.alive:
        print("ALIVING GAME")
        start_game()
    else:
        draw_game()
def mousePressed():
    global homepage
    homepage.handle_mouse_press(mouseX, mouseY)
    game.drag(mouseX,mouseY)
        
  
