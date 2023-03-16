# ===== NUMPY => FOR MATRIX =====
# import numpy as np

# list_a = {1,2,3,4,}
# vector_a = np.array([1,2,3,4,])

# print(list_a)
# print(vector_a)


# ===== PY GAME =====
import pygame
# init
pygame.init()

# variable running game
isRun = True

# membuat display sirface object
window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width, window_height))


# object game
# posisi
x = 250
y = 250

height = 20
width = 20
speed = 1


while isRun:
    # pygame.time.delay(10)
    # user input, databse input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
    

    # take all keyboard press
    keys = pygame.key.get_pressed()

    # left
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    
    # right
    if keys[pygame.K_RIGHT] and x < window_width - width:
        x += speed

    # down
    if keys[pygame.K_DOWN] and y < window_width - height:
        y += speed

    # up
    if keys[pygame.K_UP] and  y > 0:
        y -= speed



    # update asset
    window.fill((255,255,255))
    pygame.draw.rect(window, (255,0,0), (x,y, height, width))

    # render to display
    pygame.display.update()
    

pygame.quit()



