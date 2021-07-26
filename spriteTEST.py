import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, scale, pos_x, pos_y):
        super().__init__()

        self.is_animating = False

        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/walking_1.png'), (scale, scale)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/walking_2.png'), (scale, scale)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/walking_3.png'), (scale, scale)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/walking_4.png'), (scale, scale)))


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

        return pos_x, pos_y

    def animate(self):
        self.is_animating = True

    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.1

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                #self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]


pygame.init()
fps = pygame.time.Clock()

#screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = SCREEN_WIDTH
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("animation test")

GRAY = (100, 100, 100)

moving_sprites = pygame.sprite.Group()
player = Player(250, 10,10)
moving_sprites.add(player)

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = not running

        if event.type == pygame.KEYDOWN:
            player.animate()
            player(pos_x) += 5

    SCREEN.fill(GRAY)
    moving_sprites.draw(SCREEN)
    moving_sprites.update()
    pygame.display.flip()
    fps.tick(60)