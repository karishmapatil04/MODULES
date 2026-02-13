import pygame  
  
pygame.init()  
screen = pygame.display.set_mode((400, 300))  
done = False  
  
while not done:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
    pygame.draw.rect(screen, (160, 20, 0), pygame.Rect(200, 100, 100, 60))    
  
    pygame.display.flip()  