# Flappy Bird Game
import pygame
import random
import sys

# Initialize Pygame
pygame.init()
# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60
GRAVITY = 0.5
BIRD_JUMP = -10
PIPE_GAP = 150
PIPE_FREQUENCY = 1500  # milliseconds
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")
# Load images
bird_image = pygame.image.load("bird.png").convert_alpha()
pipe_image = pygame.image.load("pipe.png").convert_alpha()
background_image = pygame.image.load("background.png").convert()


# Bird class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0
        self.image = bird_image
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def jump(self):
        self.velocity = BIRD_JUMP

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        self.rect.center = (self.x, self.y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# Pipe class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(100, 400)
        self.top_rect = pygame.Rect(self.x, 0, pipe_image.get_width(), self.height)
        self.bottom_rect = pygame.Rect(
            self.x,
            self.height + PIPE_GAP,
            pipe_image.get_width(),
            SCREEN_HEIGHT - self.height - PIPE_GAP,
        )

    def update(self):
        self.x -= 3
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x
