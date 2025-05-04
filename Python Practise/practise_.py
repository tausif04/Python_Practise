import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Object with Fireworks")

# Font
font = pygame.font.SysFont("Arial", 36, bold=True)

# Ball properties
ball_color = WHITE
ball_radius = 20
ball_x = 50
ball_y = HEIGHT // 2
ball_speed = 5

# Fireworks function
def draw_firework():
    for _ in range(20):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT // 2)
        color = random.choice([RED, YELLOW, BLUE])
        size = random.randint(2, 5)
        pygame.draw.circle(screen, color, (x, y), size)

# Main loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    # Draw fireworks
    draw_firework()

    # Draw ball
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    # Draw text
    text = font.render("Everything will be OK", True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT - 50))

    # Update ball position
    ball_x += ball_speed
    if ball_x - ball_radius > WIDTH:
        ball_x = -ball_radius

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Refresh the screen
    pygame.display.flip()
    clock.tick(30)

# Quit pygame
pygame.quit()
sys.exit()
