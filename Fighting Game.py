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


#ermmmmm this is scrapped i just dont like deleting code in case i need it 
'''class Ground():
        def __init__(self):
                self.rect= pygame.Rect((0, 805, 1920, 1))


        def draw(self, surface, color):
                pygame.draw.rect(surface, color, self.rect)
GROUND= Ground()'''
class Fighter():
        def __init__(self, x, y):
                self.flip= False
                self.x= x
                self.y= y
                self.rect= pygame.Rect((x, y, 80, 180))
                
                self.vy= 0
                
                self.attack_type=0
                self.attacking= False
                
                self.health= 100
                
                self.width= 63
                self.height= 137

                self.animation_loop= 1
                self.facing= 'right'
                self.image= CerealGuy.get_sprite(51, 468, self.width, self.height)
                self.rect= self.image.get_rect()
                self.rect.x= self.x
                self.rect.y= self.y


               

                
        def attack(self, surface, target):
          self.attacking= True
          attacking_rect= pygame.Rect(self.rect.centerx-(2*self.rect.width*self.flip), self.rect.y, 2* self.rect.width, self.rect.height)
          if attacking_rect.colliderect(target.rect):
            target.health -= 10
          pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
        '''def load_images(self, spritesheet, animation_steps):
          for i in range(animation):
            temporary= spritesheet.subsurface('''

        def update(self):
          self.animate()
        


        def animate(self):
          key = pygame.key.get_pressed()

          if self.facing=='right':
            self.image= CerealGuy.get_sprite(51, 468, self.width, self.height)
          else:
            self.image= CerealGuy.get_sprite(51, 611, self.width, self.height)
                       

          left_animations = [CerealGuy.get_sprite(40, 300, self.width, self.height), CerealGuy.get_sprite(40, 300, self.width, self.height), CerealGuy.get_sprite(157, 300, self.width, self.height),
                       CerealGuy.get_sprite(293, 300, self.width, self.height)]

          
          if self.facing=="left" and key[pygame.K_a]:
            self.image =  left_animations[math.floor(self.animation_loop)]
            self.animation_loop +=0.1
            if self.animation_loop >=4:
              self.animation_loop = 1
            
            
          
        
        def move(self, surface, target):
          #scrapped method to prevent character from going into the depths of hell
                '''if int(self.rect.centery)+90 >805:
                        self.rect.centery=715
                        print(self.rect.centery)'''
                        
                #idk why screen_width is here im just scared to delete it
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

                #ok but like this is the dumbest logic error ive ever had when dealing with code; i fixed it and it all but like it gave me a headache when the only "problem" was the that it was "in the wrong spot" smd
                if key[pygame.K_r] or key[pygame.K_t]:
                  if self.attacking==False:
                    #^^^this works now btw; checks if the player attacked. Pretty much prevents spamming or holding in attack buttons
                    self.attack(surface, target)
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
                        self.vy=0
                        dy= 805- self.rect.bottom

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
  
  



  

fighter_1= Fighter(200, 310)
fighter_2= Fighter(700, 310)






pygame.display.update()
#game loop

run= True
while run:

        clock.tick(FPS)
        
        draw_background()
        draw_health_bar(fighter_1.health, 20, 20)
        draw_health_bar(fighter_2.health, 1500, 20)

        #move fighters
        fighter_1.move(screen, fighter_2)
        #fighter_2.move(screen, fighter_1)
        #fighter_2.move()
        fighter_1.draw(screen, (0, 0, 0))
        fighter_2.draw(screen, (0, 0, 0))
        if fighter_1.x>fighter_2.x: #omg this works
          fighter_1.facing='left'
          fighter_2.facing='right'
        else:
          fighter_1.facing='right'
          fighter_2.facing= 'left'
        fighter_1.update()
        fighter_2.update()
        
    
    #event handler
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run= False
    
    #update display
        pygame.display.update()
        
#exit pygame
pygame.quit()


