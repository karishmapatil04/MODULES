import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Custom Event Example")

# Initial colors
color1 = (255, 0, 0)
color2 = (0, 0, 255)

# Sprite positions
rect1 = pygame.Rect(200, 250, 100, 100)
rect2 = pygame.Rect(500, 250, 100, 100)

# Create custom event
CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 2000)  # trigger every 2 seconds

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Custom event: change colors
        if event.type == CHANGE_COLOR:
            color1 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            color2 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    # Background
    screen.fill((255, 255, 255))

    # Draw sprites
    pygame.draw.rect(screen, color1, rect1)
    pygame.draw.rect(screen, color2, rect2)

    # Update display
    pygame.display.update()

pygame.quit()
sys.exit()