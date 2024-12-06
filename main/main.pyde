# importing relevant libraries: 
# ==========================================================
import os 
import math 
import random 
import time
add_library('sound')
# add_library('gifAnimation')

# ==========================================================
# dimensions 
# ==========================================================
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
# declaring the constants:
# ==========================================================
UPPER_RAIL = 213
BOTTOM_RAIL = 635
LEFT_RAIL = 82
RIGHT_RAIL = 917
RESOLUTION_W = 1000
RESOLUTION_H = 800
BALL_RADIUS = 15

BALL_TYPES = ["cue","solid","solid","solid","solid","solid","solid","solid","8-ball","stripes","stripes","stripes","stripes","stripes","stripes","stripes"]

# positions = [
#     (240, 275, 1), (210, 260, 2), (210, 290, 3), (180, 245, 4),
#     (180, 305, 15), (150, 230, 5), (150, 260, 6), (150, 290, 7),
#     (180, 275, 8), (150, 320, 9), (120, 215, 10), (120, 245, 11),
#     (120, 275, 12), (120, 305, 13), (120, 335, 14)
# ]
positions = [
    (210, 260), (210, 290), (180, 245),
    (180, 305), (150, 230), (150, 260), (150, 290),
    (150, 320), (120, 215), (120, 245),
    (120, 275), (120, 305), (120, 335)
]

FRICTION = 0.02

is_game_over = False

# ==========================================================
# loading the media
# ==========================================================
cue = loadImage(PATH + "/media/" +"ball_0.png")
table = loadImage(PATH + "/media/" +"table.png")
stick = loadImage(PATH + "/media/" +"stick.png")
cross = loadImage(PATH + "/media/" +"cross.png")
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

avatar = [loadImage(PATH + "/media/" +"avatar1.png"),loadImage(PATH + "/media/" +"avatar2.png")]
highlight = loadImage(PATH + "/media/" +"glow2.png")
text_box = loadImage(PATH + "/media/" + "text_box.png")

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
main_bg = loadImage(PATH + "/media/" + "main_bg.png")


# ==========================================================
# Sounds Class:
# ==========================================================
class Sound:
    def __init__(self):
        self.collision_sound = collision_sound
        self.strong_collision_sound = strong_collision_sound
        self.pocket_sound = pocket_sound
        self.mario_sound = mario_sound
        self.is_sound_on = True
        self.volume_level = 1.0
        self.is_decreasing = True
        
    def play_collision_sound(self):
        #this function plays the collision sound when balls collide 
            self.strong_collision_sound.play()
    
    def play_pocket_sound(self):
        # this function plays the pocket sound when a ball is pocketed
        self.pocket_sound.play()
    
    def play_mario_sound(self):
        # this function plays the background music yippee
        self.mario_sound.play()
        self.mario_sound.loop()
        self.mario_sound.amp(self.volume_level)
        
    def toggle_sound(self):
        #this function controls the mechanism for the sound button on the homepage 
        if not self.is_sound_on:            
            self.mario_sound.loop()
            self.is_sound_on = True             
        else:
            if self.is_decreasing:
                # Decrease volume if sound is on
                self.volume_level = max(0.0, self.volume_level - 0.1)  # Cap volume at 0.0
                if self.volume_level == 0.0:
                    self.is_decreasing = False
            else:
                self.volume_level = min(1.0, self.volume_level + 0.1)
                if self.volume_level == 1.0:
                    self.is_decreasing = True       

            self.mario_sound.amp(self.volume_level)


# ==========================================================
# Point Class:
# ==========================================================
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


# ==========================================================
# Ball Class:
# ==========================================================
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
        v = max(0,v*(1-FRICTION))
        if abs(v) < 0.01:
            v = 0
        self.velocity.x = v*cos(theta)*(-1 if self.velocity.x<0 else 1)
        self.velocity.y = v*sin(theta)*(-1 if self.velocity.y<0 else 1)
        
    def collide(self, other):
        game.has_collided=1
        if self.velocity.x>0 or self.velocity.y>0:
            sound_manager.play_collision_sound()
        if game.first_collision==None:
            game.first_collision=other.type
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
        else:
            self.velocity.x,self.velocity.y=0,0
        
    def display(self):
        if not self.is_pocketed:
            imageMode(CENTER)
            image(self.img,self.position.x,self.position.y)
            imageMode(CORNER)

# ==========================================================
# cueball class 
# ==========================================================
class CueBall(Ball):
    def __init__(self,x,y,ID):
        Ball.__init__(self,x,y,ID)
        self.is_in_hand=False
        
    def in_hand(self):
        self.is_in_hand=True
        
    def track(self,distance):
        x,y=mouseX-self.position.x,mouseY-self.position.y
        angle = math.atan(float(y) / (x)) if x!=0 else PI/2
        if(x>0 and y<0):
            angle = PI+angle
        elif (x>=0 and y>=0):
            angle = PI+angle
        elif (x<0 and y>0):
            angle = 2*PI+angle
        distance+=100
        tracker = Point(distance*-cos(angle)+self.position.x,distance*-sin(angle)+self.position.y)
        # print(tracker.x,tracker.y)
        if(game.is_static() and not self.is_in_hand):
            fill(255,0,0)
            circle(tracker.x,tracker.y,5)
            pushMatrix()
            # rotateX(-angle)
            # rotateY(-angle)
            # angle*=-1
            angle+=PI
            rotate(angle)
            new_x = tracker.x *math.cos(-angle) - (tracker.y)*math.sin(-angle)
            new_y = (tracker.y)*math.cos(-angle)+ tracker.x*math.sin(-angle)
            image(stick, new_x, new_y)
            popMatrix()
            angle-=PI
            stroke(3)
            # strokeFill(220, 220, 220)
            line(100*cos(angle)+self.position.x,100*sin(angle)+self.position.y,200*cos(angle)+self.position.x,200*sin(angle)+self.position.y)
            # game.complete_break()
            # game.next_turn()
        return angle
    
    def is_colliding(self):
        for ball in game.balls:
            distance = math.sqrt((ball.position.x-self.position.x)**2+(ball.position.y-self.position.y)**2)
            if distance<=2*BALL_RADIUS:
                return 1
        return 0
    
    def place(self):
        if not self.is_colliding() and not self.is_pocketed:
            self.is_in_hand=0

    def display(self):
        if self.is_in_hand and (self.is_colliding() or self.is_pocketed):
            imageMode(CENTER)
            image(cross,self.position.x,self.position.y,30,30)
            imageMode(CORNER)
        else:
            Ball.display(self)
            
    def update(self):
        if(self.is_in_hand):
            self.is_pocketed=0
            self.position.x=mouseX
            self.position.y=mouseY
        Ball.update(self)
        
        
# ==========================================================
# Player class
# ==========================================================
class Player:
    def __init__(self, name, id):
        self.name = name 
        self.id = id
        self.side = -1 if self.id == 1 else 1
        self.group = None
        self.list_of_balls = []
        self.is_turn=0
        
    def assign(self, group):
        print("player "+str(self.id)+" was assigned "+group)
        self.group = group
        
    def draw_placeholders(self):
        # this function makes the placeholders for the balls of each player
        positions = [(RESOLUTION_W/2 +self.side*410, 100), (RESOLUTION_W/2 +self.side*370, 100), 
                     (RESOLUTION_W/2 +self.side*330, 100), (RESOLUTION_W/2 +self.side*290, 100), 
                     (RESOLUTION_W/2 +self.side*250, 100), (RESOLUTION_W/2 +self.side*210, 100), 
                     (RESOLUTION_W/2 +self.side*170 , 100)]
        noStroke()
        for x, y in positions:
            fill(0,0,0) 
            ellipse(x, y, 33, 33)
            if(len(self.list_of_balls)):
                ball = self.list_of_balls.pop()
                imageMode(CENTER)
                image(ball.img,x,y,30,30)
                imageMode(CORNER)
                
    def draw_avatars(self):
        imageMode(CENTER)
        image(avatar[self.id-1], RESOLUTION_W/2 +self.side*100, 70, 100, 100)
        imageMode(CORNER)
        
        fill(0,0,0)
        if self.is_turn:
            fill(15, 30, 120)
        textSize(20)
        # textFont(font)
        fill(255)
        textAlign(CENTER)
        text("Player "+str(self.id), RESOLUTION_W/2 + self.side*200, 50)
        
    def update(self):
        for ball in game.balls:
            if ball.type==self.group and not ball.is_pocketed:
                self.list_of_balls.append(ball)
        if not self.list_of_balls and self.group!=None and self.group!='8-ball':
            self.group = '8-ball'
            self.update()
            
    def display(self):
        self.update()
        if self.is_turn:
            # print("displaying highlights")
            imageMode(CENTER)
            image(highlight, RESOLUTION_W/2 +self.side*100, 70, 200, 200)
            imageMode(CORNER)
        self.draw_placeholders()
        self.draw_avatars()

# textbox class
class TextBox:
    def __init__(self):
        self.foul_message = None
        self.turn_message = None
        self.show_text_box = False
        self.starting_player_text = None
        
    def display_text_box(self):
        # print(self.show_text_box, self.starting_player_text)
        if self.show_text_box and self.foul_message:
            image(text_box, 200, 710, 600, 80)
            #textFont(font)  
            fill(255) 
            textAlign(CENTER)
            text(self.foul_message, 200 + text_box.width / 2, 719 + text_box.height / 2)
        elif self.show_text_box and self.turn_message:
            image(text_box, 200, 710, 600, 80)
            fill(255) 
            textAlign(CENTER)
            text(self.turn_message, 200 + text_box.width / 2, 719 + text_box.height / 2)
        elif self.show_text_box and self.starting_player_text:
            image(text_box, 200, 710, 600, 80)
            fill(255) 
            textAlign(CENTER)
            text(self.starting_player_text, 200 + text_box.width / 2, 719 + text_box.height / 2)
        

# Game Class
# ==========================================================
class Game:
    def __init__(self):
        positions = [
    (210, 260), (210, 290), (180, 245),
    (180, 305), (150, 230), (150, 260), (150, 290),
    (150, 320), (120, 215), (120, 245),
    (120, 275), (120, 305), (120, 335)
]
        self.alive=0
        self.balls = []
        self.balls.append(Ball(240+30, 275+150, 1))
        self.balls.append(Ball(180+30, 275+150, 8))
        rest_of_balls = [2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15]
        random.shuffle(rest_of_balls)
        for n in rest_of_balls:
            x,y=positions.pop()
            self.balls.append(Ball(int(x + 30), int(y + 150), int(n)))
        for ball in self.balls:
            print(ball.position.x,ball.position.y,ball.ID)

    
        self.players = [Player("Player 1",1),Player("Player 2",2)]
        self.starting_player = None
        self.game_state = "SHOW_STARTING_PLAYER"
        
        self.cue = CueBall(700,275+150,0)
        # seballs.append(cue)
        self.pockets =[]
        self.in_hit=0
        self.curx=0
        self.cury=0
        self.in_play=0
        self.is_break=1
        self.has_collided=0
        self.first_collision=None
        self.textbox = TextBox()     
        self.turn = self.pick_starting_player()  
        
    def start(self):
        print("I AM ALIVE")
        self.alive=1
        
    def ball_in_hand(self):
        self.cue.in_hand()
        # self.cue = CueBall(700,275+150,0)

    def game_over(self): #<============================ THIS THIS
        global is_game_over
        is_game_over=True
        print('I DIED')
        textSize(128)
        gameoverpage.draw_gameover_page()
        
    def pick_starting_player(self):
        turn = random.choice([0,1])
        self.starting_player = self.players[turn]    
        self.textbox.starting_player_text = str(self.starting_player.name) + " starts the game and gets to break <3"   
        self.textbox.show_text_box = True
        self.players[turn].is_turn=1
        return turn
    
    def switch_turns(self):
        self.players[self.turn].is_turn=0
        self.turn=1-self.turn
        self.players[self.turn].is_turn=1
        self.textbox.turn_message = "Current turn:" + " " + str(self.players[self.turn].name)
        self.textbox.show_text_box = True
        
    def assign_groups_on_first_pocket(self, ball, current_player, opponent):
        if not current_player.group and ball.type in ["solids", "stripes"]:
            current_player.assign_group(ball.type)
            opponent.assign_group("solids" if ball.type == "stripes" else "stripes")  
                      
    def handle_mouse_press(self,x,y):
        if not self.cue.is_in_hand:
            self.drag(x,y)
        else:
            self.cue.place()
            self.textbox.show_text_box = True
            self.textbox.foul_message = None
            self.textbox.turn_message = "Current turn:" + " " + str(self.players[self.turn].name)
            print("TextBox updated - Turn Message:", {self.textbox.turn_message}, "Show:", {self.textbox.show_text_box})
            
    def drag(self,x,y):
        if self.alive:
            # print("555")
            self.in_hit=1
            self.curx=x
            self.cury=y
            
    def is_static(self):
        flag=self.cue.velocity.x==0 and self.cue.velocity.y==0
        for ball in self.balls:
            if not ball.is_pocketed:
                flag &=ball.velocity.x==0 and ball.velocity.y==0
        return flag
    
    def hit(self,x,y):
        self.in_hit=0
        if self.alive and (self.curx !=0 or self.cury!=0) and not self.in_play:
            if math.sqrt((x-self.cue.position.x)**2+(y-self.cue.position.y)**2)<=math.sqrt((self.curx-self.cue.position.x)**2+(self.cury-self.cue.position.y)**2):
                return
            self.in_play=1
            distance = math.sqrt((x-self.curx)**2+(y-self.cury)**2)
            distance/=13
            angle = self.cue.track(distance)
            print('RELEASED')
            self.cue.hit(distance,angle)
            self.in_play=1
        
    def check_collision(self,ball1,ball2):
        distance = math.sqrt((ball1.position.x-ball2.position.x)**2+(ball1.position.y-ball2.position.y)**2)
        if distance<=2*BALL_RADIUS:
            ball1.collide(ball2)
            
    def evaluate_turn(self):
        print("TURN ENDED")
        pocketed_balls=[]
        for ball in self.balls:
            if ball.is_pocketed:
                pocketed_balls.append(ball)
                self.balls.remove(ball)
        pocketed = {'stripes':0,'solid':0,'8-ball':0}
        for ball in pocketed_balls:
            pocketed[ball.type]=1
                
        print(pocketed['stripes'], pocketed['solid'])

        if pocketed['8-ball']:
            print("8-ball IS POCKETED FOUL - (GAME OVER)")
            self.textbox.foul_message = "FOUL : 8-Ball was pocketed - GAME OVER!"
            self.textbox.show_text_box = True
            self.game_over()
        elif self.cue.is_pocketed:
            print("CUE IS POCKETED FOUL")
            self.textbox.foul_message = "FOUL : Cue ball was pocketed!"
            self.textbox.show_text_box = True
            self.switch_turns()
            self.ball_in_hand()
        elif self.has_collided==0:
            print("NO HIT FOUL")
            self.textbox.foul_message = "FOUL : No ball was hit!"
            self.textbox.show_text_box = True
            self.switch_turns()
            self.ball_in_hand()
        elif self.first_collision!=self.players[self.turn].group and self.players[self.turn].group!=None:
            print("OPPONENT BALL HIT FIRST FOUL") 
            self.textbox.foul_message = "FOUL : Opponent's ball hit first!"
            self.textbox.show_text_box = True
            self.switch_turns()
            self.ball_in_hand()
        elif ((len(pocketed_balls)==0) or (self.players[self.turn].group !=None and not pocketed[self.players[self.turn].group])):
            self.switch_turns()
        elif not self.players[self.turn].list_of_balls and self.players[self.turn].group!=None:
            self.game_over()
            
        if not self.is_break and pocketed['stripes']+pocketed['solid']==1 and self.players[self.turn].group==None:
            if pocketed['solid']:
                self.players[self.turn].assign("solid")
                self.players[1-self.turn].assign("stripes")
            else:
                self.players[1-self.turn].assign("solid")
                self.players[self.turn].assign("stripes") 
                
        self.is_break=0
        self.has_collided=0
        self.first_collision=None
        
    def update(self):
        for ball in self.balls:
            ball.update()
        # print("UPDATING GAME")
        self.cue.update()
        for ball1 in self.balls:
            for ball2 in self.balls:
                if (ball1.ID == ball2.ID):
                    continue
                self.check_collision(ball1,ball2)
            if not self.cue.is_in_hand:
                self.check_collision(self.cue,ball1)
        if(self.in_play and self.is_static()):
            self.in_play=0
            self.evaluate_turn()
    
    def display(self):
        if self.alive:
            # print("TESTTT")
            image(main_bg, 0, 0, RESOLUTION_W, RESOLUTION_H)
            image(table, 20, 150, RESOLUTION_W - 40, RESOLUTION_H - 250)
            distance = math.sqrt((mouseX-self.curx)**2+(mouseY-self.cury)**2)
            distance/=10
            self.cue.track(distance if self.in_hit else 0)
            self.update()
            # print(self.cue.velocity.x,self.cue.velocity.y)
            for ball in self.balls:
                ball.display()
            self.players[0].display()
            self.players[1].display()
            fill(255,255,255)
            textAlign(CENTER)
            # text(str(self.textbox.starting_player_text), RESOLUTION_W/2, 180)
            # self.cue.track(distance if self.in_hit else 0)
            self.cue.display()
            self.textbox.display_text_box()


        stroke(3)
        line(110, 213, 462, 213)
        line(525, 213, 884, 213)
        line(110, 635, 462, 635)
        line(525, 635, 884, 635)
        line(82, 246, 82, 602)
        line(917, 246, 917, 602)
        
        
# ==========================================================
# Button class 
# ==========================================================
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
            
            
# ==========================================================
# Homepage class
# ==========================================================
class HomePage:
    def __init__(self):
        self.buttons = []
        self.home_page_image = home_page_image
        self.on_home_page = True
        self.on_instructions_page = False
        self.setup_buttons()
        
    def setup_buttons(self):
        self.buttons.append(Button(350, 300, 320, 110, play_button, self.start_game))
        self.buttons.append(Button(450, 400, 100, 100, help_button, self.show_instructions))
        self.buttons.append(Button(450, 500, 100, 100, sound_button, self.toggle_sound))
        self.buttons.append(Button(350, 600, 320, 110, quit_button, self.quit_game))

    def draw_home_page(self):
        background(0)
        image(self.home_page_image, 0, 0, RESOLUTION_W, RESOLUTION_H, 211, 0, 1498, 1080)
        for button in self.buttons:
            button.display()
    def quit_game(self):
        exit()
        
    def toggle_sound(self):
        print("Toggling sound")
        
    def start_game(self):
        self.on_home_page = False
        game.start()
        
    def toggle_sound(self):
        sound_manager.toggle_sound()
        
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
# gameover class 
# ==========================================================
class GameOverPage:
    def __init__(self):
        self.buttons = []
        self.game_over_page_image = home_page_image
        self.on_game_over_page = True
        self.setup_buttons()
        
    def setup_buttons(self):
        self.buttons.append(Button(350, (RESOLUTION_H / 2) +100, 320, 110, play_button, self.restart_game))
        self.buttons.append(Button(350, 600, 320, 110, quit_button, self.quit_game))

    def draw_gameover_page(self):
        game.alive=0
        background(0)
        image(self.game_over_page_image, 0, 0, RESOLUTION_W, RESOLUTION_H, 211, 0, 1498, 1080)
        for button in self.buttons:
            button.display()
        textSize(50)
        text("Game Over!", RESOLUTION_W / 2, (RESOLUTION_H / 2) -70)
        text("Player "+str(game.players[game.turn].id)+" Wins! Yayy!!", RESOLUTION_W / 2, RESOLUTION_H / 2)
        text("Play again?", RESOLUTION_W / 2, (RESOLUTION_H / 2) +70)
        
    def quit_game(self):
        exit()
        is_game_over = False

    def restart_game(self):
        global is_game_over, game, homepage
        is_game_over = False
        game=Game()
        homepage= HomePage()
        sound_manager = Sound()

    def handle_mouse_press(self, mouse_x, mouse_y):
        for button in self.buttons:
            if button.is_hovered(mouse_x, mouse_y):
                button.handle_click()


# ==========================================================
game = Game()
homepage = HomePage()
gameoverpage = GameOverPage()
sound_manager = Sound()
# ==========================================================


def setup():
    size(RESOLUTION_W, RESOLUTION_H)
    sound_manager.play_mario_sound()
    # game.setup()
    # mario_sound.play() 
    # mario_sound.loop()
    
def draw():
    background(255,255,255)
    global homepage
    if homepage.on_home_page:
        homepage.draw_home_page()
    elif homepage.on_instructions_page:
        homepage.draw_instructions_page()
    # elif not game.alive:
    #     print("ALIVING GAME")
    #     # homepage.start_game()
    elif is_game_over:
        gameoverpage.draw_gameover_page()
    else:
        game.display()
        
def mousePressed():
    global homepage, gameoverpage, is_game_over
    game.handle_mouse_press(mouseX,mouseY)
    homepage.handle_mouse_press(mouseX, mouseY)
    if is_game_over:
        gameoverpage.handle_mouse_press(mouseX, mouseY)
    else:
        homepage.handle_mouse_press(mouseX, mouseY)
        
def mouseReleased():
    game.hit(mouseX,mouseY)
    
    
  
