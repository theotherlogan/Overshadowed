import pygame

class Enemy(pygame.sprite.Sprite):
    #this is the class for the three main plant enemies, and creates a new object based on type
    #also takes parameters for scale and position

    def __init__(self, type, scale, pos_x, pos_y):
        super().__init__()

        #setting the current frame
        self.current_frame = 0
        #making the type option accessible to all methods
        self.type = type

        #squirter enemy
        if self.type == "squirter":        
            self.squirter = []
            self.squirter.append(pygame.transform.scale(pygame.image.load('assets/squirter_1.png'),(scale, scale)))
            self.squirter.append(pygame.transform.scale(pygame.image.load('assets/squirter_2.png'),(scale, scale)))
            self.squirter.append(pygame.transform.scale(pygame.image.load('assets/squirter_3.png'),(scale, scale)))
            self.squirter.append(pygame.transform.scale(pygame.image.load('assets/squirter_4.png'),(scale, scale)))

            #setting up the image and rect, plus position
            self.image = self.squirter[self.current_frame]
            self.rect = self.image.get_rect()
            self.rect.topleft = [pos_x, pos_y]

        #vine enemy
        elif self.type == "vine":
            self.vine = []
            self.vine.append(pygame.transform.scale(pygame.image.load('assets/vine_1.png'),(scale, scale)))
            self.vine.append(pygame.transform.scale(pygame.image.load('assets/vine_2.png'),(scale, scale)))
            self.vine.append(pygame.transform.scale(pygame.image.load('assets/vine_3.png'),(scale, scale)))

            self.image = self.vine[self.current_frame]
            self.rect = self.image.get_rect()
            self.rect.topleft = [pos_x, pos_y]
        
        #flytrap enemy
        elif self.type == "flytrap":
            self.flytrap = []
            self.flytrap.append(pygame.transform.scale(pygame.image.load('assets/flytrap_1.png'),(scale, scale)))
            self.flytrap.append(pygame.transform.scale(pygame.image.load('assets/flytrap_2.png'),(scale, scale)))
            self.flytrap.append(pygame.transform.scale(pygame.image.load('assets/flytrap_3.png'),(scale, scale)))
            self.flytrap.append(pygame.transform.scale(pygame.image.load('assets/flytrap_4.png'),(scale, scale)))

            self.image = self.flytrap[self.current_frame]
            self.rect = self.image.get_rect()
            self.rect.topleft = [pos_x, pos_y]


    #animation with rate (fps) option
    def animate(self, rate):

        if self.type == "squirter":
            #setting the animation loop rate
            self.current_frame += rate

            #reset frame condition
            if self.current_frame >= len(self.squirter):
                self.current_frame = 0

            #changing the frame based on the int of the loop rate
            self.image = self.squirter[int(self.current_frame)]

        #same for vines
        elif self.type == "vine":
            self.current_frame += rate

            if self.current_frame >= len(self.vine):
                self.current_frame = 0

            self.image = self.vine[int(self.current_frame)]

        #same for flytrap
        elif self.type == "flytrap":
            self.current_frame += rate

            if self.current_frame >= len(self.flytrap):
                self.current_frame = 0

            self.image = self.flytrap[int(self.current_frame)]

#basic game set up
pygame.init()
fps = pygame.time.Clock()

#screen
SCREEN_WIDTH = 700
SCREEN_HEIGHT = SCREEN_WIDTH
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("enemy animation test")

#colors
WHITE = (255, 255, 255)

#enemy group and initiation
enemies = pygame.sprite.Group()
squirter = Enemy("squirter", 250, 450, 450)
vines = Enemy("vine", 300, 0,0)
flytrap = Enemy("flytrap", 300, 0, 400)
enemies.add(squirter)
enemies.add(vines)
enemies.add(flytrap)

#game loop
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = not running

    #no need for conditions, these always animate throughout
    squirter.animate(0.15)
    vines.animate(0.15)
    flytrap.animate(0.15)

    #basic screen fill and updating the groups, fps
    SCREEN.fill(WHITE)
    enemies.draw(SCREEN)
    enemies.update()
    pygame.display.flip()
    fps.tick(60)
