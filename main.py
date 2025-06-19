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

    def draw(self, surface):
        surface.blit(pipe_image, (self.x, self.top_rect.y), self.top_rect)
        surface.blit(pipe_image, (self.x, self.bottom_rect.y), self.bottom_rect)

    def collide(self, bird):
        return self.top_rect.colliderect(bird.rect) or self.bottom_rect.colliderect(
            bird.rect
        )


def draw_text(surface, text, size, x, y, color=WHITE):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)


def main():
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = []
    score = 0
    running = True
    last_pipe = pygame.time.get_ticks()
    game_over = False

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    bird.jump()
                if event.key == pygame.K_r and game_over:
                    main()  # Restart game

        if not game_over:
            bird.update()
            # Add new pipes
            now = pygame.time.get_ticks()
            if now - last_pipe > PIPE_FREQUENCY:
                pipes.append(Pipe(SCREEN_WIDTH))
                last_pipe = now

            # Update pipes
            for pipe in pipes:
                pipe.update()

            # Remove off-screen pipes
            pipes = [pipe for pipe in pipes if pipe.x + pipe_image.get_width() > 0]

            # Collision detection
            for pipe in pipes:
                if pipe.collide(bird):
                    game_over = True

            # Check if bird hits ground or goes above screen
            if bird.y > SCREEN_HEIGHT or bird.y < 0:
                game_over = True

            # Scoring
            for pipe in pipes:
                if (
                    not hasattr(pipe, "scored")
                    and pipe.x + pipe_image.get_width() < bird.x
                ):
                    score += 1
                    pipe.scored = True

        # Draw everything
        screen.blit(background_image, (0, 0))
        for pipe in pipes:
            pipe.draw(screen)
        bird.draw(screen)
        draw_text(screen, f"Score: {score}", 36, SCREEN_WIDTH // 2, 50)

        if game_over:
            draw_text(
                screen, "GAME OVER", 64, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, RED
            )
            draw_text(
                screen,
                "Press R to Restart",
                32,
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2 + 60,
                WHITE,
            )

        pygame.display.flip()


if __name__ == "__main__":
    main()
