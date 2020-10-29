import pygame
from constants import screen_width,screen_height,RED

class Ball:
    def __init__(self):
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.velocity_x = 5
        self.velocity_y = 5
        self.radius = 10

    def draw(self,screen):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.radius)

    def getRect(self):
        return pygame.Rect(
            self.x, self.y, self.radius * 2,self.radius * 2
        )

    def tick(self,paddle_left,paddle_right):
        self.x += self.velocity_x
        self.y += self.velocity_y

        if self.y > screen_height - self.radius * 2:
            self.velocity_y *= -1

        if self.x > screen_width - self.radius * 2:
            self.velocity_x *= -1

        if self.x < self.radius * 2:
            self.velocity_x *= -1

        if self.y < self.radius * 2:
            self.velocity_y *= -1

        if self.getRect().colliderect(paddle_left.rect):
            self.velocity_x *= -1

        if self.getRect().colliderect(paddle_right.rect):
            self.velocity_x *= -1