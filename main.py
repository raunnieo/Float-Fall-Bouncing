#importing Modules
import pygame 
from sys import exit #To close the window
import random #To genrate random variables
import loadScreen
import vectors
import menu

#Initializing PyGame
pygame.init()

#Screen Setup
window_height = 793
window_width = 1410
screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE) #Makes a window
pygame.display.set_caption('Float Fall Bouncing') #Sets the name of the window
clock = pygame.time.Clock() #To add time delay in game loop
show_load = True

output = {"Menu": False, "Ball":1}
#Making required surfaces
bg_surface = pygame.image.load('graphics/bg/bg.png').convert()
bg_grd = pygame.image.load('graphics/bg/bground.png').convert_alpha()
bg_water = pygame.image.load('graphics/water/water.png').convert()
bg_moon = pygame.image.load('graphics/moon/moonsky.png').convert()
bg_moongrd = pygame.image.load('graphics/moon/moongrd.png').convert_alpha()
midscene = pygame.image.load('graphics/Scenes/enter2.png').convert()
legend = pygame.image.load(('graphics/Scenes/legends.png')).convert_alpha()

#Ball class to store and control properties of body aka ball
class Ball:
    t=0.1
    balls = []
    def __init__(self, x, y, g, type):
        self.x = x
        self.y = y
        self.type = type
        self.e = 0.7*(1 + (self.type-1)*0.1) #Coefficient of restitution
        self.g = g
        self.gNet = g
        self.v_x = 0
        self.v_y = 0
        self.f = 0.001 #Drag Coefficient
        self.density = 1
        self.volume = 0.08
        self.mass = self.density*self.volume
        self.ball_surface = pygame.image.load(f'graphics/ball/{self.type}.png').convert_alpha()
        self.ball_rect = self.ball_surface.get_rect(midbottom = (self.x,self.y))
        self.dragging = False
        
        Ball.balls.append(self)
    
    def drag(self):
         #Assuming drag directly proportional to -kv
         self.v_x += -self.v_x*self.f
         self.v_y += -self.v_y*self.f

    def update_position(self):
            disp_y = (self.v_y*Ball.t+0.5*(self.gNet)*Ball.t**2)*10  #s = ut + 0.5at**2
            self.v_y += (self.gNet)*Ball.t  #v=u+at
            self.ball_rect.bottom += disp_y #updates the coordinates of the bottom most point
            self.y = self.ball_rect.bottom #the update coordinates are stored in y value
            if self.y < 0:
                self.remove_ball()
    def replot_x(self,scale):
        self.ball_rect.left *= scale
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
ball1 = Ball(window_width//2, window_height-130, 10, output["Ball"]) #Creating a Ball object
back = 0 #To count current scene
back_dict = {0:10, 1:1, 2:1.6} #Stores value of acceleration due to gravitation force.
#In back_dict the value for key = 1 is density of the medium rather than acceleration value
c_pressed = False #To check if c key is pressed.
mousebutton = False
esc = False

#Font generation
text_font = pygame.font.Font("graphics/font/gooddog-plain.regular.ttf",40)

if show_load:
    #Showing waiting screen
    while loadScreen.load_screen(screen):
        continue
    #Showing loading Screen
    while loadScreen.loading(screen):
        continue

size = screen.get_size()
scale = round(size[0]/window_width, 2)
bottomline = window_height-130*scale #To set the collision point

if size[0]!=window_width:
    bg_surface = pygame.transform.scale_by(bg_surface, scale)
    bg_grd = pygame.transform.scale_by(bg_grd, scale)
    bg_water = pygame.transform.scale_by(bg_water, scale)
    bg_moon = pygame.transform.scale_by(bg_moon, scale)
    bg_moongrd = pygame.transform.scale_by(bg_moongrd, scale)
    midscene = pygame.transform.scale_by(midscene, scale)
    for i in Ball.balls:
        i.replot_x(scale)
    window_height = size[1]
    window_width = size[0]
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)

#Main loop
while True:
    ball_pos = []
    for i in Ball.balls:
        ball_pos.append((i.x-150, i.x+150))

    #Rendering the text to show density of the medium
    add_surface = text_font.render(f'Density of medium = {(round(back_dict[1], 2))}', None, 'Black')
    add_rect = add_surface.get_rect(topleft = (25,25))

    #To detect any event taking place
    for event in pygame.event.get():
        #Quit and close the window if Close Button(X) is pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.VIDEORESIZE:
            scale = round(event.w/window_width, 2)
            for i in Ball.balls:
                i.replot_x(scale)
            window_height = event.h
            window_width = event.w
            screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
            bg_surface = pygame.image.load('graphics/bg/bg.png').convert()
            bg_grd = pygame.image.load('graphics/bg/bground.png').convert_alpha()
            bg_water = pygame.image.load('graphics/water/water.png').convert()
            bg_moon = pygame.image.load('graphics/moon/moonsky.png').convert()
            bg_moongrd = pygame.image.load('graphics/moon/moongrd.png').convert_alpha()
            midscene = pygame.image.load('graphics/Scenes/enter2.png').convert()
            legend = pygame.image.load(('graphics/Scenes/legends.png')).convert_alpha()
            print(scale)
            bg_surface = pygame.transform.scale_by(bg_surface, scale)
            bg_grd = pygame.transform.scale_by(bg_grd, scale)
            bg_water = pygame.transform.scale_by(bg_water, scale)
            bg_moon = pygame.transform.scale_by(bg_moon, scale)
            bg_moongrd = pygame.transform.scale_by(bg_moongrd, scale)
            midscene = pygame.transform.scale_by(midscene, scale)
            
        elif event.type == pygame.KEYDOWN:
             #Changing the y velocity of ball when Space key is pressed
             for i in Ball.balls:
                if event.key == pygame.K_SPACE and abs(i.v_y)<5 and (i.ball_rect.bottom > window_height-round(135*scale) and back == 0):
                    i.v_y = -random.randint(15, 34)
                if event.key == pygame.K_SPACE and (abs(i.v_y)<=1 and back == 1):
                    i.v_y = -random.randint(6, 10)
                if event.key == pygame.K_SPACE and abs(i.v_y)<5 and (i.ball_rect.bottom > window_height-round(160*scale) and back == 2):
                    i.v_y = -random.randint(6, 9)
             #Adding new balls
             if event.key == pygame.K_a and len(Ball.balls)<3 : #Limits the maximum number of balls to 3
                #Adding balls at different position depending on the scene
                ready = False
                x = random.randint(50, window_width-50)
                if len(Ball.balls)==0:
                    ready = True
                while not ready:
                    for pos in ball_pos:
                        if x not in range(pos[0], pos[1]):
                            ready = True
                        else:
                            ready = False
                            x = random.randint(50, window_width-50)
                if back == 0:
                    ball = Ball(x, bottomline, 10, output["Ball"])
                elif back == 1:
                    ball = Ball(x, bottomline, 10, output["Ball"])
                else:
                    ball = Ball(x, 0, 10, output["Ball"])
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
             elif event.key == pygame.K_h:
                 for i in Ball.balls:
                     i.ball_rect.bottom = 200
                     i.v_y = 0

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
                 interactive = not interactive
             if event.key == pygame.K_ESCAPE:
                 esc = not esc

        elif event.type == pygame.MOUSEBUTTONDOWN and interactive:
             mousebutton = True
             for i in Ball.balls:
                  if i.ball_rect.collidepoint(event.pos):
                       i.dragging = True
                       curr_ball = i

        elif event.type == pygame.MOUSEBUTTONUP or interactive == False:
            
             for i in Ball.balls:
                  i.dragging = False
             mousebutton = False
             curr_ball = None
   
        if interactive:
            if event.type == pygame.MOUSEBUTTONDOWN and len(Ball.balls) < 3:
                dragger = True
                for i in Ball.balls:
                        dragger = dragger and i.dragging
                if not dragger or len(Ball.balls) == 0:
                    if 50<=event.pos[0]<=window_width-50 and 50<=event.pos[1]<=bottomline-50:
                        ball = Ball(event.pos[0], event.pos[1], 10, output["Ball"])
    if interactive:
        if mousebutton and curr_ball != None:
            curr_ball.ball_rect.center = pygame.mouse.get_pos()
            curr_ball.v_y = 0

    screen.blit(bg_surface, (0,0)) #Adds the background on the screen

    if esc:
        output_new = menu.menu(screen)
        for props in output_new:
            if output_new[props] != output[props]:
                output[props] = output_new[props]
        if not interactive:
            for i in Ball.balls:
                i.type = output["Ball"]
                i.ball_surface = pygame.image.load(f'graphics/ball/{i.type}.png').convert_alpha()
        esc = False

    else:
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
                bottomline = window_height
            elif back == 0:
                screen.blit(bg_surface, (0,0))
                screen.blit(bg_grd, (0, 0))
                bottomline = window_height- round(130*scale)
            elif back == 2:
                screen.blit(bg_moon, (0,0))
                screen.blit(bg_moongrd, (0,0))
                bottomline = window_height-round(155*scale)

            screen.blit(legend, (window_width-150, 0)) #To add legends on screen

        #Basic Physics and mechanics
        for i in Ball.balls:
                screen.blit(i.ball_surface, i.ball_rect.topleft) #Shows ball on screen
                vectors.show_vectors(screen, i) #To show vectors of each ball
                i.sense_medium(back_dict[back]) #Tracks medium
                i.drag() #Applies drag
                i.update_position()
                if i.ball_rect.bottom>=bottomline: #Collision Detection
                    i.ball_rect.bottom = bottomline
                    if 0<=abs(i.v_y)<=3:
                        i.v_y = 0
                    elif i.v_y>0:
                        i.v_y = -i.v_y*i.e

    pygame.display.update() #To update screen by showing newly blit surfaces
    clock.tick(30) #Adds delay of 30ms
