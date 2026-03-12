import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Level Up Game")

# Load background image
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (800, 600))

# Load sound
pygame.mixer.init()
sound = pygame.mixer.Sound("sound.wav")

# Initial colors
color1 = (255, 0, 0)
color2 = (0, 0, 255)

# Sprites
sprite1 = pygame.Rect(200, 250, 100, 100)
sprite2 = pygame.Rect(500, 250, 100, 100)

# Custom event
CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 2000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Custom event to change color and play sound
        if event.type == CHANGE_COLOR:
            color1 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            color2 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            sound.play()

    # Draw background
    screen.blit(background, (0, 0))

    # Draw sprites
    pygame.draw.rect(screen, color1, sprite1)
    pygame.draw.rect(screen, color2, sprite2)

    # Update display
    pygame.display.update()

pygame.quit()
sys.exit()