import pygame
import random
from pygame.math import Vector2

class Game:
    def __init__(self, ruby_group, player_group, platform_group):
        self.music = pygame.mixer.music.load('sounds/game_sound.wav')
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play(-1)
        self.message_font = pygame.font.Font('fonts/Poultrygeist.ttf', size=64)
        self.font_hud = pygame.font.Font('fonts/Pixel.ttf')
        # self.tile1_image = pygame.transform.scale(pygame.image.load('images/tiles/Tile (2).png').convert_alpha(),(32, 32))
        self.tile_images = [pygame.transform.scale(pygame.image.load(f'images/tiles/Tile ({n+1}).png').convert_alpha(),(32, 32)) for n in range(5)]

        self.platform_group = platform_group
        self.player_group = player_group
        self.ruby_group = ruby_group
        # tile map size is 23 rows and 40 columns
        self.tile_map = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,'P', 0, 0, 0, 0, 0, 'R', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [4, 4, 4, 4, 4, 4, 4 ,4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4 ,4, 4, 4, 4, 4],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4 ,4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [4 ,4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [4, 4, 4, 4, 4, 4, 4, 4 ,4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4 ,4, 4, 4, 4, 4, 4, 4],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

        self.making_map()
        self.openning_messege()

    def making_map(self):
        for i in range(23):
            for j in range(40):
                if self.tile_map[i][j] == 1:
                    Tiles(self.tile_images[0], 32 * j, 32 * i, self.platform_group)
                if self.tile_map[i][j] == 2:
                    Tiles(self.tile_images[1], 32 * j, 32 * i, self.platform_group)
                if self.tile_map[i][j] == 3:
                    Tiles(self.tile_images[2], 32 * j, 32 * i, self.platform_group)
                if self.tile_map[i][j] == 4:
                    Tiles(self.tile_images[3], 32 * j, 32 * i, self.platform_group)
                if self.tile_map[i][j] == 5:
                    Tiles(self.tile_images[4], 32 * j, 32 * i, self.platform_group)
                if self.tile_map[i][j] == 'P':
                    self.player = Player(32 * j, 32 * i - 32, self.platform_group, self.player_group)
                if self.tile_map[i][j] == 'R':
                    self.mother_ruby = Rubies(32 * j, 32 * i - 32, self.ruby_group)

    def openning_messege(self):
        self.title = self.message_font.render('Zombie Knight', True, 'green')
        self.title_rect = self.title.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
        self.message_begin = self.message_font.render("Press 'Enter' to Begin", True, 'white')
        self.message_begin_rect = self.message_begin.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 80))
        display_surface.blit(self.title, self.title_rect)
        display_surface.blit(self.message_begin, self.message_begin_rect)
        pygame.display.update()
        self.pause_game()

    def pause_game(self):
        is_wait = True
        while is_wait:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        is_wait = False

class Tiles(pygame.sprite.Sprite):
    def __init__(self, image, x, y, groups):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)

class Player(pygame.sprite.Sprite):
        def __init__(self, x, y, platform_group, groups):
            super().__init__(groups)
            self.player_size = 64

            self.player_idle_animation_right = [pygame.transform.scale(pygame.image.load(f'images/player/idle/Idle ({n+1}).png').convert_alpha(), (self.player_size, self.player_size)) for n in range(10)]
            self.player_idle_animation_left = [pygame.transform.flip(image, True, False) for image in self.player_idle_animation_right]
            self.player_attack_animation_right = [pygame.transform.scale(pygame.image.load(f'images/player/attack/Attack ({n+1}).png').convert_alpha(), (self.player_size, self.player_size)) for n in range(10)]
            self.player_attack_animation_left = [pygame.transform.flip(image, True, False) for image in self.player_attack_animation_right]
            self.player_jump_animation_right = [pygame.transform.scale(pygame.image.load(f'images/player/jump/Jump ({n+1}).png').convert_alpha(), (self.player_size, self.player_size)) for n in range(10)]
            self.player_jump_animation_left = [pygame.transform.flip(image, True, False) for image in self.player_jump_animation_right]
            self.player_run_animation_right = [pygame.transform.scale(pygame.image.load(f'images/player/run/Run ({n+1}).png').convert_alpha(), (self.player_size, self.player_size)) for n in range(10)]
            self.player_run_animation_left = [pygame.transform.flip(image, True, False) for image in self.player_run_animation_right]

            self.image = self.player_idle_animation_right[0]
            self.rect = self.image.get_rect(topleft=(x, y))
            self.mask = pygame.mask.from_surface(self.image)

            self.animation_number = 0
            self.animation_sprite = self.player_run_animation_left

            # kinematic constants
            self.HORIZONTAL_ACCELERATION = 0.5
            self.HORIZONTAL_FRICTION = 0.05
            self.VERTICAL_ACCELERATION = 0.5
            self.VERTICAL_JUMP_SPEED = 13.5

            # kinematic initial values
            self.position = Vector2(x, y)
            self.velocity = Vector2(0, 0)
            self.acceleration = Vector2(0, self.VERTICAL_ACCELERATION)

            self.is_grounded = False
            self.facing = 'right'
            self.platform_group = platform_group

        def update(self):
            self.move()
            self.animation()
            self.check_status()
            self.choose_animation()

        def animation(self):
            self.animation_number += 0.2
            if self.animation_number >= len(self.animation_sprite):
                self.animation_number = 0
            else:
                self.image = self.animation_sprite[int(self.animation_number)]

        def jump(self):
            if self.is_grounded:
                self.velocity.y = -1 * self.VERTICAL_JUMP_SPEED

        def check_status(self):

            collided_platform = pygame.sprite.spritecollideany(self, self.platform_group,pygame.sprite.collide_mask)
            if collided_platform:
                if self.velocity.y > 0:
                    self.is_grounded = True
                    self.velocity.y = 0
                    self.position.y = collided_platform.rect.top - 58
                elif self.velocity.y < 0:
                
                    self.velocity.y = 0
                    self.position.y = collided_platform.rect.bottom

            else:
                self.is_grounded = False
        
        def choose_animation(self):

            if self.is_grounded:
                if self.facing == 'right':
                    if self.velocity.x > 1:
                        self.animation_sprite = self.player_run_animation_right
                    else:
                        self.animation_sprite = self.player_idle_animation_right
                else:
                    if self.velocity.x < -1:
                        self.animation_sprite = self.player_run_animation_left
                    else:
                        self.animation_sprite = self.player_idle_animation_left                     
        


        def move(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                self.acceleration.x = self.HORIZONTAL_ACCELERATION
                self.facing = 'right'
            elif keys[pygame.K_LEFT]:
                self.acceleration.x = - self.HORIZONTAL_ACCELERATION
                self.facing = 'left'
            else:
                self.acceleration.x = 0

            # calculate kinemetic values
            self.acceleration.x -= self.velocity.x * self.HORIZONTAL_FRICTION
            self.velocity += self.acceleration
            self.position += self.velocity + 0.5 * self.acceleration
            
            self.wrap_around_motion()
            
            # change the rect
            self.rect.topleft = (int(self.position.x), int(self.position.y))

        def wrap_around_motion(self):
            if self.position.x < 0:
                self.position.x = WINDOW_WIDTH - self.player_size
            elif self.position.x + self.player_size > WINDOW_WIDTH:
                self.position.x = 0

class Rubies(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.ruby_size = 64
        self.ruby_animation = [pygame.transform.scale(pygame.image.load(f'images/ruby/sprite_ruby{n}.png').convert_alpha(), (self.ruby_size, self.ruby_size)) for n in range(7)]
        self.animation_sprite = self.ruby_animation
        self.animation_number = 0
        self.image = self.ruby_animation[self.animation_number]
        self.rect = self.image.get_rect(topleft=(x, y))


    def update(self):

        self.animation()

    def animation(self):
        # print(self.animation_number)
        self.animation_number += 0.15
        if self.animation_number >= len(self.animation_sprite):
            self.animation_number = 0
        else:
            self.image = self.animation_sprite[int(self.animation_number)]



# initialize pygame
pygame.init()

# set display surface
WINDOW_WIDTH = 1280  #1280/32=40
WINDOW_HEIGHT = 736    #736/32=23
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Zombie Knight')

# background
background_image = pygame.image.load('images/background.png')
background_rect = background_image.get_rect(topleft=(0,0))
# set clock and FPS
clock = pygame.time.Clock()
FPS =60

# sprite groups
platform_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
ruby_group = pygame.sprite.Group()

my_game = Game(ruby_group, player_group, platform_group)
my_player = my_game.player


# main game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_SPACE:
                my_player.jump()


    # fill the background
    display_surface.blit(background_image, background_rect)
    platform_group.draw(display_surface)
    player_group.update()
    player_group.draw(display_surface)
    ruby_group.update()
    ruby_group.draw(display_surface)

    # update the display
    pygame.display.update()

    # tick the clock
    clock.tick(FPS)

# end the game
pygame.quit()
