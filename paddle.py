import pygame

from constants import PADDLE_HEIGHT,screen_height,RED


class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(0,screen_height // 2 - PADDLE_HEIGHT / 2,20,PADDLE_HEIGHT)
        self.SPEED = 10

    def draw(self,screen):
        pygame.draw.rect(screen,RED,self.rect)

    def move_up(self):
        self.rect.y -= self.SPEED
        self.keep_in_bounds()

    def move_down(self):
        self.rect.y += self.SPEED
        self.keep_in_bounds()

    def keep_in_bounds(self):
        self.rect.y = min(self.rect.y,screen_height - self.rect.height)
        self.rect.y = max(0,self.rect.y)