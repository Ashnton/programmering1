import pygame
import sys
import random

pygame.init()

# Starta Skärm
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Spelinställningar
GAMESPEED = 5
LEVEL = 5

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
restart_game = False
last_pressed = None
eaten = True
score = 0
obstacles_x = []
obstacles_y = []
obstacle_amount = 0
amount_changed = True
global_counter = 0
removal_time = 0

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

def check_collision_snake(head_x, head_y, snake_x, snake_y):
    for i in range(1, len(snake_x)):
        if (head_x == snake_x[i] and head_y == snake_y[i]):
            return True

def check_obstacle_collision(snake_x, snake_y, obstacle_x, obstacle_y):
    if len(obstacle_x) and len(obstacle_y):
        snake_set = set(zip(snake_x, snake_y))
        obstacle_set = set(zip(obstacle_x, obstacle_y))
        
        if (snake_set.intersection(obstacle_set)):
            return True

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
      
def rand_obstacles(amount, snake_x, snake_y):
    obstacles_x = []
    obstacles_y = []
    
    for i in range(amount):
        invalid_position = True
        
        while invalid_position:
            obstacle_temp_x = random.randint(0, 29)*20
            obstacle_temp_y = random.randint(0, 29)*20
            # if not check_collision_snake(obstacle_temp_x, obstacle_temp_y, snake_x, snake_y) and not check_collision(food_x, food_y, height, width, obstacle_temp_x, obstacle_temp_y):
            if not check_collision_snake(obstacle_temp_x, obstacle_temp_y, snake_x, snake_y):
                obstacles_x.append(obstacle_temp_x)
                obstacles_y.append(obstacle_temp_y)
                invalid_position = False
        
    return [obstacles_x, obstacles_y]
    
def move_towards_snake(snake_x, snake_y, enemy_x, enemy_y, blocksize):
    targetX = snake_x[0]
    targetY = snake_y[0]
    
    for i in range(len(enemy_x)):        
        if enemy_x[i] < targetX:
            newX = enemy_x[i] + blocksize
        if enemy_y[i] < targetY:
            newY = enemy_y[i] + blocksize
        if enemy_x[i] > targetX:
            newX = enemy_x[i] - blocksize
        if enemy_y[i] > targetY:
            newY = enemy_y[i] - blocksize
        if enemy_x[i] == targetX:
            newX = enemy_x[i]
        if enemy_y[i] == targetY:
            newY = enemy_y[i] 
        
        if not check_collision_snake(newX, newY, enemy_x, enemy_y) and not check_collision_snake(newX, newY, snake_x, snake_y):
            enemy_x[i] = newX
            enemy_y[i] = newY

def dist_to_snake(x_cord, y_cord, snake_x, snake_y, blocksize):
    return abs(snake_x[0] - x_cord)/20 + abs(snake_y[0] - y_cord)/blocksize + 5

# Setup inför spelstart
if LEVEL == 1:
    pass
elif LEVEL == 2:
    obstacle_amount = 10
    [obstacles_x, obstacles_y] = rand_obstacles(obstacle_amount, snake_x, snake_y)
elif LEVEL == 4:
    obstacle_amount = 10
    [obstacles_x, obstacles_y] = rand_obstacles(obstacle_amount, snake_x, snake_y)


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
                if last_pressed == "left" and len(snake_x) > 1:
                    game_over = True
                
                last_pressed = "right"
            elif event.key == pygame.K_LEFT:
                if last_pressed == "right" and len(snake_x) > 1:
                    game_over = True
                    
                last_pressed = "left"
            elif event.key == pygame.K_UP:
                if last_pressed == "down" and len(snake_x) > 1:
                    game_over = True
                    
                last_pressed = "up"
            elif event.key == pygame.K_DOWN:
                if last_pressed == "up" and len(snake_x) > 1:
                    game_over = True
                    
                last_pressed = "down"

    # Matlogik
    while eaten:
        foodX = random.randint(0, 29)*20
        foodY = random.randint(0, 29)*20
        if not check_collision_snake(foodX, foodY, snake_x, snake_y):
            eaten = False
            
            # Specifikt för nivåer där maten ska försvinna efter en tid
            if LEVEL == 5:
                removal_time = dist_to_snake(foodX, foodY, snake_x, snake_y, width) + 2
        
        
    # Spellogik
    print(removal_time)
    
    if check_collision(snake_x[-1], snake_y[-1], width, height, foodX, foodY, foodWidth, foodHeight):
        eaten = True
        score += 1
        amount_changed = False
        snake_x.append(snake_x[-1])
        snake_y.append(snake_y[-1])
        
        GAMESPEED *=1.1
    
    move_snake(snake_x, snake_y, last_pressed)
    
    if LEVEL == 3:
        if snake_x[0] < 0:
            for i in range(len(snake_x)):
                snake_x[i] = snake_x[i] + SCREEN_WIDTH
        elif snake_x[0] >= 600:
            for i in range(len(snake_x)):
                snake_x[i] = snake_x[i] - SCREEN_WIDTH
        elif snake_y[0] < 0:
            for i in range(len(snake_y)):
                snake_y[i] = snake_y[i] + SCREEN_HEIGHT
        elif snake_y[0] >= 600:
            for i in range(len(snake_y)):
                snake_y[i] = snake_y[i] - SCREEN_HEIGHT
    elif LEVEL == 4:
        if global_counter % 4 == 0:
            move_towards_snake(snake_x, snake_y, obstacles_x, obstacles_y, width)
            
        if score % 5 == 0 and score != 0 and not amount_changed:
            obstacle_amount += 2
            [obstacles_x, obstacles_y] = rand_obstacles(obstacle_amount, snake_x, snake_y)
            
            amount_changed = True
    else:
        if snake_x[0] < 0 or snake_x[0] >= 600 or snake_y[0] < 0 or snake_y[0] >= 600:
            game_over = True 
    
    if check_collision_snake(snake_x[0], snake_y[0], snake_x, snake_y):
        game_over = True
    if check_obstacle_collision(snake_x, snake_y, obstacles_x, obstacles_y):
        game_over = True
    
    # Utmålningskod
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), (foodX, foodY, foodWidth, foodHeight))
    
    # Loop för att rita ut ormen
    for i in range(len(snake_x)):
        pygame.draw.rect(screen, (0, 0, 255), (snake_x[i], snake_y[i], width, height))
        
    # Loop för att rita ut hinder
    for i in range(len(obstacles_x)):
        pygame.draw.rect(screen, (0, 255, 0), (obstacles_x[i], obstacles_y[i], width, height))
    
    # Skriver ut poängen på skärmen
    font = pygame.font.Font('freesansbold.ttf', 32)
    # text = font.render('Din poäng: ' + str(score), True, (0,0,0), (200,200,200))
    text = font.render('Din poäng: ' + str(score), True, (0,0,0))
    textRect = text.get_rect()
    screen.blit(text, textRect)
    
    pygame.display.update()

    clock.tick(GAMESPEED)
    
    # Uppdaterar räknare
    global_counter +=1
    removal_time -= 1
    
    if removal_time == 0:
        eaten = True

pygame.quit()
quit()