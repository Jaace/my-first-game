import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('My First Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# This is relative to the WORKING DIRECTORY.
# Running this program outside of that will cause this to fail.
# TODO: Is there a better way than just using the full path?
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My First Game', False, 'Black')

# I want to make my snail move faster when stretched out and slower when in,
# with acceleration. Should be doable, even if not in tutorial.
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600

# STOPPING AT 54:06

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0, 300))
    screen.blit(text_surface,(300, 50))
    snail_x_pos -= 4
    if snail_x_pos < -100:
        snail_x_pos = 800
    screen.blit(snail_surface,(snail_x_pos, 265))

    pygame.display.update()
    clock.tick(60)