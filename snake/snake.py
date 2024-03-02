import pygame
import sys
import random

pygame.init()

# Starta Skärm
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

# Spelinställningar
GAMESPEED = 5

# Egenskaper ormhuvud
positionX = 40
positionY = 100
width = 20
height = 20

# Egenskaper orm
snake_x = [positionX]
snake_y = [positionY]

# Egenskaper mat
foodX = None
foodY = None
foodWidth = 20
foodHeight = 20

# Spelvariabler
game_over = False
last_pressed = None
eaten = True

# Funktioner för spelet
def check_collision(x1, y1, width1, height1, x2, y2, width2, height2):
    # Beräkna koordinaterna för bounding box för båda objekten
    left1 = x1
    right1 = x1 + width1
    top1 = y1
    bottom1 = y1 + height1

    left2 = x2
    right2 = x2 + width2
    top2 = y2
    bottom2 = y2 + height2

    # Kolla om bounding box för objekt 1 överlappar med bounding box för objekt 2
    if right1 > left2 and left1 < right2 and bottom1 > top2 and top1 < bottom2:
        # Kollision har inträffat
        return True
    else:
        # Ingen kollision
        return False

def move_snake(x_list, y_list, direction):
    for i in range(len(x_list)-1, 0, -1):
        x_list[i] = x_list[i-1]
        y_list[i] = y_list[i-1]
        
    if direction == "right":
        x_list[0] += 20
    elif direction == "left":
        x_list[0] -= 20
    elif direction == "up":
        y_list[0] -= 20
    elif direction == "down":
        y_list[0] += 20
    
    return x_list, y_list
        

while not game_over:
    # Tangenthantering
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                game_over = True
            elif event.key == pygame.K_RIGHT:
                last_pressed = "right"
            elif event.key == pygame.K_LEFT:
                last_pressed = "left"
            elif event.key == pygame.K_UP:
                last_pressed = "up"
            elif event.key == pygame.K_DOWN:
                last_pressed = "down"

    # Matlogik
    if eaten:
        foodX = random.randint(0, 29)*20
        foodY = random.randint(0, 29)*20
        
        eaten = False
        GAMESPEED *=1.1
        
    # Spellogik
    
    if check_collision(snake_x[-1], snake_y[-1], width, height, foodX, foodY, foodWidth, foodHeight):
        eaten = True
        snake_x.append(snake_x[-1])
        snake_y.append(snake_y[-1])
        
        print(snake_x)    
        print(snake_y)    
    
    move_snake(snake_x, snake_y, last_pressed)
    
    # Utmålningskod
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), (foodX, foodY, foodWidth, foodHeight))
    
    # Loop för att rita ut ormen
    for i in range(len(snake_x)):
        pygame.draw.rect(screen, (0, 0, 255), (snake_x[i], snake_y[i], width, height))
        
    pygame.display.update()

    clock.tick(GAMESPEED)

pygame.quit()
quit()