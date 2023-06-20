#importing Modules
import pygame 
from sys import exit #To close the window
import random #To genrate random variables
import loadScreen
import vectors

#Initializing PyGame
pygame.init()

#Screen Setup
window_height = 650
window_width = 1000
screen = pygame.display.set_mode((window_width, window_height)) #Makes a window
pygame.display.set_caption('GravitySim') #Sets the name of the window
clock = pygame.time.Clock() #To add time delay in game loop

#Making required surfaces
bg_surface = pygame.image.load('graphics/bg/bg.png').convert()
bg_grd = pygame.image.load('graphics/bg/bground.png').convert()
bg_water = pygame.image.load('graphics/water/water.png').convert()
bg_moon = pygame.image.load('graphics/moon/moonsky.png').convert()
bg_moongrd = pygame.image.load('graphics/moon/moongrd.png').convert_alpha()
midscene = pygame.image.load('graphics/Scenes/enter2.png').convert()
legend = pygame.image.load(('graphics/Scenes/legends.png')).convert_alpha()

#Ball class to store and control properties of body aka ball
class Ball:
    t=0.1
    balls = []
    def __init__(self, x, y, g):
        self.x = x
        self.y = y
        self.e = 0.7 #Coefficient of restitution
        self.g = g
        self.gNet = g
        self.v_x = 0
        self.v_y = 0
        self.f = 0.001 #Drag Coefficient
        self.density = 1
        self.volume = 0.08
        self.mass = self.density*self.volume
        self.ball_surface = pygame.image.load('graphics/ball/1.png').convert_alpha()
        self.ball_rect = self.ball_surface.get_rect(midbottom = (self.x,self.y))
        self.dragging = False
        
        Ball.balls.append(self)
    
    def drag(self):
         #Assuming drag directly proportional to -kv
         self.v_x += -self.v_x*self.f
         self.v_y += -self.v_y*self.f

    def update_position(self):
            disp_y = (self.v_y*Ball.t+0.5*(self.gNet)*Ball.t**2)*20  #s = ut + 0.5at**2
            self.v_y += (self.gNet)*Ball.t  #v=u+at
            self.ball_rect.bottom += disp_y #updates the coordinates of the bottom most point
            self.y = self.ball_rect.bottom #the update coordinates are stored in y value
            if self.y < 0:
                self.remove_ball()

    def remove_ball(self):
        if len(Ball.balls)>0:
            Ball.balls.remove(self) #Remove ball from the balls list in Ball class

    def sense_medium(self, density):
        #To determine the surrounding medium of the body
        
        for i in range(len(Ball.balls)): #To update gNet of each ball with the value defined of g defined in back_dict for different scenes
            Ball.balls[i].gNet = back_dict[back]
        if back == 1:
            #Calculating buoyant force due to medium
            #Assumed ball to be cube
            fb = 0
            for i in Ball.balls:
                if i.ball_rect.bottom>280:
                    if 280<i.ball_rect.bottom<=380:
                        fb = density*self.g*(self.ball_rect.bottom-280)*self.volume/(self.mass*100)
                        i.f = 0.01
                    else:
                        fb = density*self.g*self.volume/self.mass
                        i.f = 0.07 #If the ball is completely inside water then drag coefficeint is set to 0.07
                    i.gNet = i.g - fb
                else:
                    i.gNet = i.g
                    i.f = 0.01

#Turning on and off Interactive Mode
interactive = False
curr_ball = None
ball1 = Ball(500, 520, 10) #Creating a Ball object
back = 0 #To count current scene
back_dict = {0:10, 1:1, 2:1.6} #Stores value of acceleration due to gravitation force.
#In back_dict the value for key = 1 is density of the medium rather than acceleration value
bottomline = 520 #To set the collision point
c_pressed = False #To check if c key is pressed.

#Font generation
text_font = pygame.font.Font("graphics/font/gooddog-plain.regular.ttf",40)

#Showing waiting screen
while loadScreen.load_screen(screen):
    continue
#Showing loading Screen
while loadScreen.loading(screen):
    continue

#Main loop
while True:
    #Rendering the text to show density of the medium
    add_surface = text_font.render(f'Density of medium = {(round(back_dict[1], 2))}', None, 'Black')
    add_rect = add_surface.get_rect(topleft = (25,25))

    #To detect any event taking place
    for event in pygame.event.get():
        #Quit and close the window if Close Button(X) is pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
             #Changing the y velocity of ball when Space key is pressed
             for i in Ball.balls:
                if event.key == pygame.K_SPACE and abs(i.v_y)<5 and (i.ball_rect.bottom > 515 and back == 0):
                    i.v_y = -random.randint(10, 20)
                if event.key == pygame.K_SPACE and (abs(i.v_y)<=1 and back == 1):
                    i.v_y = -random.randint(6, 20)
                if event.key == pygame.K_SPACE and abs(i.v_y)<5 and (i.ball_rect.bottom > 490 and back == 2):
                    i.v_y = -random.randint(6, 9)
             #Adding new balls
             if event.key == pygame.K_a and len(Ball.balls)<3 : #Limits the maximum number of balls to 3
                #Adding balls at different position depending on the scene
                if back == 0:
                    ball = Ball(random.randint(50, 900), 520, 10)
                elif back == 1:
                    ball = Ball(random.randint(50, 900), 650, 10)
                else:
                    ball = ball = Ball(random.randint(50, 900), 495, 10)
             #Removing balls based on FIFO (First-in-first-out)
             elif event.key == pygame.K_r:
                    if len(Ball.balls)>0:
                        Ball.balls[0].remove_ball()
             #Changing the scenes
             elif event.key == pygame.K_c:
                 if not c_pressed: #If c_pressed == False, value of back is updated to change scene
                    if back<2:
                        back+=1
                    else:
                        back -=2
                    c_pressed = True

             if event.key == pygame.K_RETURN and c_pressed: #Checks if Enter key is pressed after c
                 c_pressed = False

             #To change the density of medium by RIGHT and LEFT arrow keys  
             if event.key == pygame.K_RIGHT and back == 1:
                 if 0.8<=back_dict[back]<1.5: #Restricts the values to be between 0.8 and 1.5
                    back_dict[back]+=0.1

             if event.key == pygame.K_LEFT and back == 1:
                 if 0.8<back_dict[back]<=1.6:
                    back_dict[back]-=0.1
            
             #Code for interactive mode
             if event.key == pygame.K_i:
                 if interactive:
                     interactive = False
                 else:
                     interactive = True

        elif event.type == pygame.MOUSEBUTTONDOWN and interactive:
             for i in Ball.balls:
                  if i.ball_rect.collidepoint(event.pos):
                       i.dragging = True
                       curr_ball = i

        elif event.type == pygame.MOUSEBUTTONUP or interactive == False:
             for i in Ball.balls:
                  i.dragging = False

        if interactive:
            for i in Ball.balls:
                if i.dragging:
                    curr_ball.ball_rect.center = pygame.mouse.get_pos()
                    curr_ball.v_y = 0
                
            if event.type == pygame.MOUSEBUTTONDOWN and len(Ball.balls) < 3:
                dragger = True
                for i in Ball.balls:
                        dragger = dragger and i.dragging
                if not dragger or len(Ball.balls) == 0:
                    if 50<=event.pos[0]<=950 and 50<=event.pos[1]<=bottomline-50:
                        ball = Ball(event.pos[0], event.pos[1], 10)

    screen.blit(bg_surface, (0,-100)) #Adds the background on the screen

    if c_pressed: #If c_pressed == True all the balls are removed and "Press Enter is shown"
        for i in Ball.balls:
            i.remove_ball()
        screen.blit(midscene, (0,0))
   
    else: 
    #Else the background is added depending on current scene
    #Also sets the bottomline of each scene
        if back == 1:
            screen.blit(bg_water, (0,0))
            screen.blit(add_surface, add_rect)
            bottomline = 650
        elif back == 0:
            screen.blit(bg_surface, (0,-100))
            screen.blit(bg_grd, (0, 480))
            bottomline = 520
        elif back == 2:
            screen.blit(bg_moon, (0,0))
            screen.blit(bg_moongrd, (0,0))
            bottomline = 495

        screen.blit(legend, (850,0)) #To add legends on screen

    #Basic Physics and mechanics
    for i in Ball.balls:
            screen.blit(i.ball_surface, i.ball_rect.topleft) #Shows ball on screen
            vectors.show_vectors(screen, i) #To show vectors of each ball
            i.sense_medium(back_dict[back]) #Tracks medium
            i.drag() #Applies drag
            i.update_position()
            if i.ball_rect.bottom>=bottomline: #Collision Detection
                i.ball_rect.bottom = bottomline
                if i.v_y>0:
                    i.v_y = -i.v_y*i.e

    pygame.display.update() #To update screen by showing newly blit surfaces
    clock.tick(20) #Adds delay of 20ms
