import pygame
import sys

# Initialize pygame
pygame.init()

# Screen size
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sprites Example")

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# Sprite positions
x = 100
y = 100
speed = 5

# Second sprite position
enemy_x = 500
enemy_y = 300

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Background
    screen.fill(white)

    # Draw movable sprite
    pygame.draw.rect(screen, blue, (x, y, 50, 50))

    # Draw second sprite (static)
    pygame.draw.rect(screen, red, (enemy_x, enemy_y, 50, 50))

    # Update display
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()