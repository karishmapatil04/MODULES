import pygame
import sys

# Initialize pygame
pygame.init()

# Set screen size
width = 800
height = 600

# Create game window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game Screen with Elements")

# Font for text
font = pygame.font.SysFont("Arial", 40)

# Create text
text = font.render("My First Game", True, (255, 255, 255))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background color
    screen.fill((0, 0, 0))

    # Draw rectangle
    pygame.draw.rect(screen, (0, 255, 0), (300, 250, 200, 100))

    # Add text
    screen.blit(text, (300, 150))

    # Update display
    pygame.display.update()

pygame.quit()
sys.exit()