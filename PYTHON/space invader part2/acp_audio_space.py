import math
import random
import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background
background = pygame.image.load(r"C:\Users\samai\OneDrive\Documents\Codingal_Learn\webdev course\MODULES\PYTHON\space invader game\space.png")
background = pygame.transform.scale(background, (800, 500))

# Background Music
pygame.mixer.music.load(r"C:\Users\samai\OneDrive\Documents\Codingal_Learn\webdev course\MODULES\PYTHON\space invader game\background.wav")
pygame.mixer.music.play(-1)  # Loop forever
pygame.mixer.music.set_volume(0.5)

# Sound Effects
bullet_sound = pygame.mixer.Sound(r"C:\Users\samai\OneDrive\Documents\Codingal_Learn\webdev course\MODULES\PYTHON\space invader game\laser.wav")
explosion_sound = pygame.mixer.Sound(r"C:\Users\samai\OneDrive\Documents\Codingal_Learn\webdev course\MODULES\PYTHON\space invader game\explosion.wav")

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load(r"C:\Users\samai\OneDrive\Documents\Codingal_Learn\webdev course\MODULES\PYTHON\space invader game\ufo.png")
icon = pygame.transform.scale(icon, (64, 64))
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load(r"C:\Users\samai\OneDrive\Documents\Codingal_Learn\webdev course\MODULES\PYTHON\space invader game\player.png")
playerImg = pygame.transform.scale(playerImg, (64, 64))
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for _i in range(num_of_enemies):
    enemy_image = pygame.image.load(r"C:\Users\samai\OneDrive\Documents\Codingal_Learn\webdev course\MODULES\PYTHON\space invader game\enemy.png")
    enemy_image = pygame.transform.scale(enemy_image, (64, 64))
    enemyImg.append(enemy_image)

    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

# Bullet
bulletImg = pygame.image.load(r"C:\Users\samai\OneDrive\Documents\Codingal_Learn\webdev course\MODULES\PYTHON\space invader game\bullet.png")
bulletImg = pygame.transform.scale(bulletImg, (16, 24))
bulletX = 0
bulletY = PLAYER_START_Y
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE

# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_sound.play()   # 🔫 Play shooting sound
                bulletX = playerX
                fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Player Movement
    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - 64))

    # Enemy Movement
    for i in range(num_of_enemies):

        if enemyY[i] > 340:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 64:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]

        # Collision
        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            explosion_sound.play()   # 💥 Play explosion sound
            bulletY = PLAYER_START_Y
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = PLAYER_START_Y
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)

    pygame.display.update()