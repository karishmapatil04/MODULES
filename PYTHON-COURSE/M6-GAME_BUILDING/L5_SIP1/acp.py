import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Create game screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Custom Event - Change Sprite Color")

# Initial colors
color1 = (255, 0, 0)
color2 = (0, 0, 255)

# Sprite rectangles
sprite1 = pygame.Rect(200, 250, 100, 100)
sprite2 = pygame.Rect(500, 250, 100, 100)

# Create custom event
CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 2000)  # event every 2 seconds

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Custom event to change sprite colors
        if event.type == CHANGE_COLOR:
            color1 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            color2 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    # Fill background
    screen.fill((255, 255, 255))

    # Draw sprites
    pygame.draw.rect(screen, color1, sprite1)
    pygame.draw.rect(screen, color2, sprite2)

    # Update screen
    pygame.display.update()

pygame.quit()
sys.exit()