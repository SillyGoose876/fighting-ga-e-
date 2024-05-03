import time
import pygame
import math
pygame.init()
YELLOW= (255, 255, 0)
RED= (255, 0, 0)
WHITE= (255, 255, 255)




BLACK= (0, 0, 0)
class Spritesheet:
  def __init__(self, file):
    self.sheet = pygame.image.load(file).convert()

  def get_sprite(self, x, y, width, height):
    sprite= pygame.Surface([width, height])
    sprite.blit(self.sheet, (0, 0), (x, y, width, height))
    sprite.set_colorkey(BLACK)
    return sprite
#create game window
SCREEN_WIDTH=1920
SCREEN_HEIGHT= 1080

screen= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ermmmm fighting game!!! guhhh")
go_image= pygame.image.load("./FGimg/the game over screen.png").convert_alpha()







#loading spritesheet
CerealGuy= Spritesheet("FGimg/spritesheet hehehe.png")


#define steps in each animation
CEREAL_ANIMATION_STEPS= [3, 3, 3, 3, 3, 3, 3] #each item in this list is the number of frames for each movement/idle animation for the character and it's spritesheet




#framerate
clock = pygame.time.Clock()
FPS= 60



#this will load the background image
background_image= pygame.image.load("./FGimg/main background i think.png").convert_alpha()

class Spritesheet: #makes a spritesheet 
  def __init__(self, file):
    self.sheet = pygame.image.load(file).convert()




class Fighter1():
        def __init__(self, x, y):
                self.flip= False
                self.x= x
                self.y= y
                self.rect= pygame.Rect((x, y, 80, 180))
                
                self.vy= 0
                
                self.attack_type=0
                self.attacking= False
                
                self.health= 100
                
                self.width= 80
                self.height= 150

                self.animation_loop= 1
                self.facing= 'right'
                self.image= CerealGuy.get_sprite(51, 468, self.width, self.height)
                self.rect= self.image.get_rect()
                self.rect.x= self.x
                self.rect.y= self.y
                self.t0= time.time()
                self.centerx= self.rect.centerx
                self.ground= True


                
  

               

                
        def attack(self, surface, target):
          attacking_rect= pygame.Rect(self.rect.centerx-(self.rect.width*self.flip), self.rect.y, self.rect.width, self.rect.height)
          if attacking_rect.colliderect(target.rect):
            target.health -= 10
            if self.facing== "right":
              target.rect.x+=100
            elif self.facing== "left":
              target.rect.x-=100
          

        
        def update(self):
          self.animate()
        


        def animate(self):
          key = pygame.key.get_pressed()

          if self.facing=='right':
            self.image= CerealGuy.get_sprite(51, 440, self.width, self.height)
          else:
            self.image= CerealGuy.get_sprite(51, 590, self.width, self.height)

            
          right_animations = [CerealGuy.get_sprite(40, 131, self.width, self.height), CerealGuy.get_sprite(40, 131, self.width, self.height), CerealGuy.get_sprite(157, 131, self.width, self.height),
                       CerealGuy.get_sprite(293, 131, self.width, self.height)]       

          left_animations = [CerealGuy.get_sprite(40, 290, self.width, self.height), CerealGuy.get_sprite(40, 290, self.width, self.height), CerealGuy.get_sprite(157, 290, self.width, self.height),
                       CerealGuy.get_sprite(293, 290, self.width, self.height)]
          attackR_animations = [CerealGuy.get_sprite(51, 740, self.width, self.height), CerealGuy.get_sprite(51, 740, self.width, self.height), CerealGuy.get_sprite(163, 740, self.width, self.height),
                       CerealGuy.get_sprite(294, 740, self.width, self.height)]
          attackL_animations = [CerealGuy.get_sprite(269, 900, self.width, self.height), CerealGuy.get_sprite(269, 900, self.width, self.height), CerealGuy.get_sprite(130, 900, self.width, self.height),
                       CerealGuy.get_sprite(29, 900, self.width, self.height)]
          
          if self.facing=="left" and key[pygame.K_a] and self.ground==True:
            self.image =  left_animations[math.floor(self.animation_loop)]
            self.animation_loop +=0.1
            if self.animation_loop >=4:
              self.animation_loop = 1
          elif self.facing=="left" and key[pygame.K_d] and self.ground==True:
            self.image =  left_animations[math.floor(self.animation_loop)]
            self.animation_loop +=0.1
            if self.animation_loop >=4:
              self.animation_loop = 1 
          elif self.facing=="right" and key[pygame.K_d] and self.ground==True:
            self.image =  right_animations[math.floor(self.animation_loop)]
            self.animation_loop +=0.1
            if self.animation_loop >=4:
              self.animation_loop = 1
          elif self.facing=="right" and key[pygame.K_a] and self.ground==True:
            self.image =  right_animations[math.floor(self.animation_loop)]
            self.animation_loop +=0.1
            if self.animation_loop >=4:
              self.animation_loop = 1
          elif self.facing=="right" and key[pygame.K_r] and self.attacking==False:
            self.image =  attackR_animations[math.floor(self.animation_loop)]
            self.animation_loop +=0.1
            if self.animation_loop >=4:
              self.animation_loop = 1
          elif self.facing=="left" and key[pygame.K_r] and self.attacking==False:
            self.image =  attackL_animations[math.floor(self.animation_loop)]
            self.animation_loop +=0.1
            if self.animation_loop >=4:
              self.animation_loop = 1

        def move(self, surface, target):
          
               
                        
                
                global SCREEN_WIDTH
                SPEED= 10
                GRAVITY=2
                dx = 0
                dy= 0
                
                #get key presses
                key = pygame.key.get_pressed()

                #can only perform other actions if not attacking
                
                if key[pygame.K_a]:
                        dx= -SPEED
                        self.x-=SPEED
                if key[pygame.K_d]:
                        dx= SPEED
                        self.x+=SPEED
                #jumping
                if key[pygame.K_w] and self.rect.bottom==805:
                        self.vy= -30

                #mg, ignore air resistence
                dy+=self.vy

                
                if key[pygame.K_r] or key[pygame.K_t]:
                  if self.dt>=0.5:
                    self.attack(surface, target)
                    self.t0= self.t1
                    #^^^this works now btw; checks if the player attacked. Pretty much prevents spamming or holding in attack buttons
                    if key[pygame.K_r]:
                      self.attack_type= 1
                    if key[pygame.K_t]:
                      self.attack_type= 2


                
                #make sure player doesn't go off screen
                if self.rect.left + dx <0:
                        dx = -self.rect.left
                if self.rect.right + dx  > SCREEN_WIDTH:
                        dx= SCREEN_WIDTH - self.rect.right
                if self.rect.bottom + dy > 805:
                        self.ground= True
                        self.vy=0
                        dy= 805- self.rect.bottom
                        
                else:
                  
                  self.ground= False
                  
                self.vy+=GRAVITY
                
                #players face each other (street fight/KOF style)
                if target.rect.centerx>self.rect.centerx:
                  self.flip=False
                else:
                  self.flip=True
                self.rect.x +=dx
                self.rect.y +=dy

        def draw(self, surface, color):
          pygame.draw.rect(surface, color, self.rect)
          surface.blit(self.image, (self.rect.x, self.rect.y))
          #classic drawing function (draws the fighter, very simple)
        def timer(self):
            self.t1 = time.time()
            self.dt = self.t1 - self.t0
            
        def setCenterx(self):
          self.centerx= self.rect.centerx
  
        
class Fighter2():
        def __init__(self, x, y):
                self.flip= False
                self.x= x
                self.y= y
                self.rect= pygame.Rect((x, y, 80, 180))
                
                self.vy= 0
                
                self.attack_type=0
                self.attacking= False
                
                self.health= 100
                
                self.width= 80
                self.height= 150

                self.animation_loop= 1
                self.facing= 'right'
                self.image= CerealGuy.get_sprite(51, 468, self.width, self.height)
                self.rect= self.image.get_rect()
                self.rect.x= self.x
                self.rect.y= self.y
                self.t0= time.time()
                self.centerx= self.rect.centerx
                self.ground= True

                
        def attack(self, surface, target):

          attacking_rect= pygame.Rect(self.rect.centerx-(self.rect.width*self.flip), self.rect.y, 0.5*self.rect.width, self.rect.height)
          if attacking_rect.colliderect(target.rect):
            target.health -= 10
            if self.facing== "right":
              target.rect.x+=100
            elif self.facing== "left":
              target.rect.x-=100
          


        def update(self):
          self.animate()
        


        def animate(self):
          key = pygame.key.get_pressed()

          if self.facing=='right':
            self.image= CerealGuy.get_sprite(51, 440, self.width, self.height)
          else:
            self.image= CerealGuy.get_sprite(51, 590, self.width, self.height)
                       
          right_animations = [CerealGuy.get_sprite(40, 131, self.width, self.height), CerealGuy.get_sprite(40, 131, self.width, self.height), CerealGuy.get_sprite(157, 131, self.width, self.height),
                       CerealGuy.get_sprite(293, 131, self.width, self.height)]             

          left_animations = [CerealGuy.get_sprite(40, 290, self.width, self.height), CerealGuy.get_sprite(40, 290, self.width, self.height), CerealGuy.get_sprite(157, 290, self.width, self.height),
                       CerealGuy.get_sprite(293, 290, self.width, self.height)]
          attackR_animations = [CerealGuy.get_sprite(51, 740, self.width, self.height), CerealGuy.get_sprite(51, 740, self.width, self.height), CerealGuy.get_sprite(163, 740, self.width, self.height),
                       CerealGuy.get_sprite(294, 740, self.width, self.height)]
          attackL_animations = [CerealGuy.get_sprite(269, 900, self.width, self.height), CerealGuy.get_sprite(269, 900, self.width, self.height), CerealGuy.get_sprite(130, 900, self.width, self.height),
                       CerealGuy.get_sprite(29, 900, self.width, self.height)]
          
          if self.facing=="left" and key[pygame.K_LEFT] and self.ground==True:
            self.image =  left_animations[math.floor(self.animation_loop)]
            self.animation_loop +=0.1
            if self.animation_loop >=4:
              self.animation_loop = 1
          elif self.facing=="left" and key[pygame.K_RIGHT] and self.ground==True:
            self.image =  left_animations[math.floor(self.animation_loop)]
            self.animation_loop +=0.1
            if self.animation_loop >=4:
              self.animation_loop = 1
          elif self.facing=="right" and key[pygame.K_LEFT] and self.ground==True:
            self.image =  right_animations[math.floor(self.animation_loop)]
            self.animation_loop +=0.1
            if self.animation_loop >=4:
              self.animation_loop = 1
          elif self.facing=="right" and key[pygame.K_RIGHT] and self.ground==True:
            self.image =  right_animations[math.floor(self.animation_loop)]
            self.animation_loop +=0.1
            if self.animation_loop >=4:
              self.animation_loop = 1
          elif self.facing=="right" and key[pygame.K_KP1] and self.attacking==False:
            self.image =  attackR_animations[math.floor(self.animation_loop)]
            self.animation_loop +=0.1
            if self.animation_loop >=4:
              self.animation_loop = 1
          elif self.facing=="left" and key[pygame.K_KP1] and self.attacking==False:
            self.image =  attackL_animations[math.floor(self.animation_loop)]
            self.animation_loop +=0.1
            if self.animation_loop >=4:
              self.animation_loop = 1
        
        def move(self, surface, target):

                global SCREEN_WIDTH
                SPEED= 10
                GRAVITY=2
                dx = 0
                dy= 0
                
                #get key presses
                key = pygame.key.get_pressed()

                #can only perform other actions if not attacking
                
                if key[pygame.K_LEFT]:
                        dx= -SPEED
                        self.x-=SPEED
                if key[pygame.K_RIGHT]:
                        dx= SPEED
                        self.x+=SPEED
                #jumping
                if key[pygame.K_UP] and self.rect.bottom==805:
                        self.vy= -30

                #gravity
                dy+=self.vy

                if key[pygame.K_KP1] or key[pygame.K_KP2]:
                  if self.dt>=0.5:
                    self.attack(surface, target)
                    self.t0= self.t1

                    if key[pygame.K_r]:
                      self.attack_type= 1
                    if key[pygame.K_t]:
                      self.attack_type= 2


                
                #make sure player doesn't go off screen
                if self.rect.left + dx <0:
                        dx = -self.rect.left
                if self.rect.right + dx  > SCREEN_WIDTH:
                        dx= SCREEN_WIDTH - self.rect.right
                if self.rect.bottom + dy > 805:
                        self.ground= True
                        self.vy=0
                        dy= 805- self.rect.bottom
                else:
                  self.ground=False
                self.vy+=GRAVITY
                
                #players face each other (street fighter/KOF style)
                if target.rect.centerx>self.rect.centerx:
                  self.flip=False
                else:
                  self.flip=True
                self.rect.x +=dx
                self.rect.y +=dy

        def draw(self, surface, color):
          pygame.draw.rect(surface, color, self.rect)
          surface.blit(self.image, (self.rect.x, self.rect.y))
          #classic drawing function (draws the fighter, very simple)

        def timer(self):
          self.t1 = time.time()
          self.dt = self.t1 - self.t0
        def setCenterx(self):
          self.centerx= self.rect.centerx
            
class Button:
  def __init__(self, x, y, width, height, fg, bg, content, fontsize):
    self.font= pygame.font.Font('JumboSale Trial.otf', fontsize)
    self.content= content
    self.x= x
    self.y= y
    self.width= width
    self.height= height

    self.fg= fg
    self.bg= bg
    self.image= pygame.Surface((self.width, self.height))
    self.image.fill(self.bg)
    self.rect= self.image.get_rect()
    self.rect.x= self.x
    self.rect.y= self.y
    self.text= self.font.render(self.content, True, self.fg)
    self.text_rect= self.text.get_rect(center=(self.width/2, self.height/2))
    self.image.blit(self.text, self.text_rect)
  def is_pressed(self, pos, pressed):
    if self.rect.collidepoint(pos):
      if pressed[0]:
        return True
      return False
    else:
      return False
def draw(screen, fighter):
    fighter.draw(self.screen)
    pygame.display.update()


def draw_background():
        screen.blit(background_image, (0, 0))


def draw_health_bar(health, x, y):
  ratio= health/ 100
  pygame.draw.rect(screen, WHITE, (x-2, y-2, 404, 34))
  pygame.draw.rect(screen, RED, (x, y, 400, 30))
  pygame.draw.rect(screen, YELLOW, (x, y, 400*ratio, 30))
  
  



  

fighter_1= Fighter1(200, 310)
fighter_2= Fighter2(700, 310)






pygame.display.update()
#game loop
font = pygame.font.Font('JumboSale Trial.otf', 32)
run= True
while run:
      
        clock.tick(FPS)
        draw_background()
        draw_health_bar(fighter_1.health, 20, 20)
        draw_health_bar(fighter_2.health, 1500, 20)
        #setting center x
        fighter_1.setCenterx()
        fighter_2.setCenterx()
        #move fighters
        fighter_1.move(screen, fighter_2)
        fighter_2.move(screen, fighter_1)
        #fighter_2.move()
        fighter_1.draw(screen, (0, 0, 0))
        fighter_2.draw(screen, (0, 0, 0))
        #timer for attacks
        fighter_1.timer()
        fighter_2.timer()
        if fighter_1.centerx>fighter_2.centerx: 
          fighter_1.facing='left'
          fighter_2.facing='right'
        else:
          fighter_1.facing='right'
          fighter_2.facing= 'left'
        fighter_1.update()
        fighter_2.update()
        if fighter_1.health<=0 or fighter_2.health<=0:
          screen.blit(go_image, (0, 0))
          
          if fighter_1.health>fighter_2.health:
            text= font.render("GAME OVER", True, BLACK)
            text_rect= text.get_rect(center=(960, 400))
            text2= font.render("Player 1 wins!!!!", True, BLACK)
            text2_rect= text.get_rect(center=(960, 500))
          elif fighter_2.health>fighter_1.health:
            text= font.render("GAME OVER", True, BLACK)
            text_rect= text.get_rect(center=(960, 400))
            text2= font.render("Player 2 wins!!!!", True, BLACK)
            text2_rect= text.get_rect(center=(960, 500))
          restart_button= Button(10, 1080 - 60, 120, 50, WHITE, BLACK, "Restart", 32)


    
        
    
    #event handler
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run= False
    
    #update display
        pygame.display.update()

#exit pygame
pygame.quit()


