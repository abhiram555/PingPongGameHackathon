import pygame
from pygame.locals import *

from constants import *
from ball import Ball
from paddle import Paddle


# Project Info
# Game version: 1.0
# author: abhiram

pygame.init()
clock = pygame.time.Clock()


# constant variable
# FPS (Frames per second)
FPS = 30

# Our Geme elements
ball = Ball()
left_paddle = Paddle()
right_paddle = Paddle()
right_paddle.rect.x = screen_width - right_paddle.rect.width




# Setting up the Main window
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Abhiram's Ping Pong Game")



# Game state
running = True

# Hanle use input
def handle_right_paddle(paddle):
    pygame.event.pump()
    keys = pygame.key.get_pressed()

    if keys[K_w]:
        paddle.move_up()
    elif keys[K_s]:
        paddle.move_down()

def handle_left_paddle(paddle):
    pygame.event.pump()
    keys = pygame.key.get_pressed()

    if keys[K_UP]:
        paddle.move_up()
    elif keys[K_DOWN]:
        paddle.move_down()

# Check for events(Event Handling)
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
            pygame.quit()
    handle_right_paddle(right_paddle)
    handle_left_paddle(left_paddle)
    screen.fill(GREEN)
    ball.draw(screen)
    ball.tick(left_paddle,right_paddle)
    left_paddle.draw(screen)
    right_paddle.draw(screen)
    pygame.display.flip()

