import pygame
import sys

# Initialize pygame
pygame.init()

# Set screen size
width = 800
height = 600

# Create game window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My First Game Screen")

# Game loop
running = True
while running:
    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen with color (RGB)
    screen.fill((0, 128, 255))

    # Update display
    pygame.display.update()

# Quit pygame
pygame.quit()
sys.exit()