import pygame
import pygame.camera
import pygame.image
import time
import sys
import random

pygame.init()

# Starta Skärm
PLAYABLE_SCREEN_WIDTH = 600
PLAYABLE_SCREEN_HEIGHT = 600

TOTAL_SCREEN_WIDTH = 800
TOTAL_SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((TOTAL_SCREEN_WIDTH, TOTAL_SCREEN_HEIGHT))
clock = pygame.time.Clock()

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

def check_collision_against_list(x1, y1, x_list, y_list):
    for i in range(len(x_list)):
        if (x1 == x_list[i] and y1 == y_list[i]):
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
      
def move_towards_snake(snake_x, snake_y, enemy_x, enemy_y, food_x, food_y, blocksize):
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
        
        if not check_collision_against_list(newX, newY, enemy_x, enemy_y) and not check_collision_against_list(newX, newY, snake_x, snake_y) and not check_collision(newX, newY, blocksize, blocksize, food_x, food_y, blocksize, blocksize):
            enemy_x[i] = newX
            enemy_y[i] = newY

def dist_to_snake(x_cord, y_cord, snake_x, snake_y, blocksize):
    return abs(snake_x[0] - x_cord)/blocksize + abs(snake_y[0] - y_cord)/blocksize + 5

def rand_obstacles(amount, snake_x, snake_y, food_x, food_y, blocksize):
    obstacles_x = []
    obstacles_y = []
    
    for i in range(amount):
        invalid_position = True
        
        while invalid_position:
            obstacle_temp_x = random.randint(0, 29)*blocksize
            obstacle_temp_y = random.randint(0, 29)*blocksize
            
            if not check_collision_against_list(obstacle_temp_x, obstacle_temp_y, snake_x, snake_y) and not check_collision(obstacle_temp_x, obstacle_temp_y, blocksize, blocksize, food_x, food_y, blocksize, blocksize) and dist_to_snake(obstacle_temp_x, obstacle_temp_y, snake_x, snake_y, blocksize) > 10:
                obstacles_x.append(obstacle_temp_x)
                obstacles_y.append(obstacle_temp_y)
                invalid_position = False
        
    return [obstacles_x, obstacles_y]

def spawn_walls(amount, wall_width, snake_x, snake_y, food_x, food_y, x_limit, y_limit, blocksize):
    wall_x = []
    wall_y = []
    
    for i in range(amount):
        invalid_position = True
        
        while invalid_position:
            [wall_temp_x, wall_temp_y] = rand_obstacles(1, snake_x, snake_y, food_x, food_y, blocksize)
            
            wall_temp_x = int(wall_temp_x[0])
            wall_temp_y = int(wall_temp_y[0])
            
            if not check_collision_against_list(wall_temp_x, wall_temp_y, snake_x, snake_y) and not check_collision(wall_temp_x, wall_temp_y, blocksize, blocksize, food_x, food_y, blocksize, blocksize) and dist_to_snake(wall_temp_x, wall_temp_y, snake_x, snake_y, blocksize) > 5 and wall_temp_x < x_limit - 5*blocksize and wall_temp_y < y_limit - 5*blocksize:
                wall_x.append(wall_temp_x)
                wall_y.append(wall_temp_y)
                
                for i in range(wall_width):
                    wall_x.append(wall_temp_x+blocksize*i)
                    wall_y.append(wall_temp_y)
                    invalid_position = False
                    
    return [wall_x, wall_y]
      
# Funktion för att visa endscreen
def show_endscreen(score):
    pygame.camera.init()

    cameras = pygame.camera.list_cameras()
            
    webcam = pygame.camera.Camera(cameras[0])

    webcam.start()
    
    # Väntar med att visa slutskärmen för att fånga användarens reaktion
    time.sleep(0.5)
    
    # Webbkameran
    
    # Hämtar bild på när användaren förlorar
    img = webcam.get_image()
    
    # Loop för endscreen
    endscreen = True
    while endscreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Tryck mellanslag för att starta om spelet
                    endscreen = False

        # Rensa skärmen
        screen.fill((255, 255, 255))


        # Rita ut text och bild på endscreen
        screen.blit(img, (0,0))

        font = pygame.font.Font('freesansbold.ttf', 24)
        text = font.render('Spelet är över!', True, (255, 0, 0))
        textRect = text.get_rect()
        textRect.center = (PLAYABLE_SCREEN_WIDTH // 2, PLAYABLE_SCREEN_HEIGHT // 2 - 50)
        screen.blit(text, textRect)

        score_text = font.render('Din poäng: ' + str(score), True, (0, 255, 0))
        score_textRect = score_text.get_rect()
        score_textRect.center = (PLAYABLE_SCREEN_WIDTH // 2, PLAYABLE_SCREEN_HEIGHT // 2)
        screen.blit(score_text, score_textRect)

        instruction_text = font.render('Tryck mellanslag för att starta om spelet', True, (0, 0, 255))
        instruction_textRect = instruction_text.get_rect()
        instruction_textRect.center = (PLAYABLE_SCREEN_WIDTH // 2, PLAYABLE_SCREEN_HEIGHT // 2 + 50)
        screen.blit(instruction_text, instruction_textRect)

        pygame.display.flip()

# Man startar på första leveln som standard
LEVEL = 1

# Färgtema
snake_color = 255, 0, 0
food_color = 0, 255, 0
obstacle_color = 0, 0, 255

while True:
    # Setup inför spelstart
    # Spelinställningar
    GAMESPEED = 5

    # Egenskaper ormhuvud
    position_x = 40
    position_x = 100
    width = 20
    height = 20

    # Egenskaper orm
    snake_x = [position_x]
    snake_y = [position_x]

    # Egenskaper mat
    food_x = 0
    food_y = 0
    food_width = 20
    food_height = 20
    

    # Spelvariabler
    game_over = False
    last_pressed = None
    eaten = True
    score = 0
    obstacles_x = []
    obstacles_y = []
    obstacle_amount = 0
    amount_changed = True
    global_counter = 0
    removal_time = 0
    display_endscreen = False

    if LEVEL == 1:
        pass
    elif LEVEL == 2:
        obstacle_amount = 10
        [obstacles_x, obstacles_y] = rand_obstacles(obstacle_amount, snake_x, snake_y, food_x, food_y, width)
    elif LEVEL == 4:
        obstacle_amount = 10
        [obstacles_x, obstacles_y] = rand_obstacles(obstacle_amount, snake_x, snake_y, food_x, food_y, width)
    elif LEVEL == 6:
        obstacle_amount = 10
        [obstacles_x, obstacles_y] = spawn_walls(obstacle_amount, 5, snake_x, snake_y, food_x, food_y, PLAYABLE_SCREEN_WIDTH, PLAYABLE_SCREEN_HEIGHT, width)

    while not game_over:
        # Tangenthantering
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    display_endscreen = True
                    
                    
                elif event.key == pygame.K_RIGHT:
                    if last_pressed == "left" and len(snake_x) > 1:
                        game_over = True
                        display_endscreen = True
                    
                    last_pressed = "right"
                elif event.key == pygame.K_LEFT:
                    if last_pressed == "right" and len(snake_x) > 1:
                        game_over = True
                        display_endscreen = True
                        
                    last_pressed = "left"
                elif event.key == pygame.K_UP:
                    if last_pressed == "down" and len(snake_x) > 1:
                        game_over = True
                        display_endscreen = True

                    last_pressed = "up"
                elif event.key == pygame.K_DOWN:
                    if last_pressed == "up" and len(snake_x) > 1:
                        game_over = True
                        display_endscreen = True

                    last_pressed = "down"
                elif event.key == pygame.K_1:
                    LEVEL = 1
                    game_over = True
                elif event.key == pygame.K_2:
                    LEVEL = 2
                    game_over = True
                elif event.key == pygame.K_3:
                    LEVEL = 3
                    game_over = True
                elif event.key == pygame.K_4:
                    LEVEL = 4
                    game_over = True
                elif event.key == pygame.K_5:
                    LEVEL = 5
                    game_over = True
                elif event.key == pygame.K_6:
                    LEVEL = 6
                    game_over = True
                elif event.key == pygame.K_r:
                    game_over = True

        # Matlogik
        while eaten:
            food_x = random.randint(0, 29)*20
            food_y = random.randint(0, 29)*20
            if not check_collision_against_list(food_x, food_y, snake_x, snake_y) and not check_collision_against_list(food_x, food_y, obstacles_x, obstacles_y):
                eaten = False
                
                # Specifikt för nivåer där maten ska försvinna efter en tid
                if LEVEL == 5:
                    removal_time = dist_to_snake(food_x, food_y, snake_x, snake_y, width) + 2 + removal_time


        # Spellogik
        
        if check_collision(snake_x[-1], snake_y[-1], width, height, food_x, food_y, food_width, food_height):
            eaten = True
            score += 1
            amount_changed = False
            snake_x.append(snake_x[-1])
            snake_y.append(snake_y[-1])
            
            GAMESPEED *=1.1
        
        move_snake(snake_x, snake_y, last_pressed)
        
        if LEVEL == 3:
            # Hanterar specialfallet på level 3 där man kan åka genom kanterna
            if snake_x[0] < 0:
                    snake_x[0] = snake_x[0] + PLAYABLE_SCREEN_WIDTH
            elif snake_x[0] >= 600:
                    snake_x[0] = snake_x[0] - PLAYABLE_SCREEN_WIDTH
            elif snake_y[0] < 0:
                    snake_y[0] = snake_y[0] + PLAYABLE_SCREEN_HEIGHT
            elif snake_y[0] >= 600:
                    snake_y[0] = snake_y[0] - PLAYABLE_SCREEN_HEIGHT
        else:
            if snake_x[0] < 0 or snake_x[0] >= 600 or snake_y[0] < 0 or snake_y[0] >= 600:
                game_over = True
                display_endscreen = True
                
                
        if LEVEL == 4:
            if global_counter % 4 == 0:
                move_towards_snake(snake_x, snake_y, obstacles_x, obstacles_y, food_x, food_y, width)
                
            if score % 5 == 0 and score != 0 and not amount_changed:
                obstacle_amount += 2
                [obstacles_x, obstacles_y] = rand_obstacles(obstacle_amount, snake_x, snake_y, food_x, food_y, width)
                
                amount_changed = True
        
        if check_collision_snake(snake_x[0], snake_y[0], snake_x, snake_y):
            game_over = True
            display_endscreen = True

        if check_obstacle_collision(snake_x, snake_y, obstacles_x, obstacles_y):
            game_over = True
            display_endscreen = True
        
        # Utmålningskod
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, food_color, (food_x, food_y, food_width, food_height))
        
        # Loop för att rita ut ormen
        for i in range(len(snake_x)):
            pygame.draw.rect(screen, snake_color, (snake_x[i], snake_y[i], width, height))
            
        # Loop för att rita ut hinder
        for i in range(len(obstacles_x)):
            pygame.draw.rect(screen, obstacle_color, (obstacles_x[i], obstacles_y[i], width, height))
        
        # Skriver ut poängen på skärmen
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Din poäng: ' + str(score), True, (0,0,0))
        textRect = text.get_rect()
        screen.blit(text, textRect)
        
        # Skriver ut leveln på skärmen
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Level: ' + str(LEVEL), True, (0, 0,0))
        textRect = (screen.get_width() - text.get_width(), 0)
        screen.blit(text, textRect)
        
        pygame.display.update()

        clock.tick(GAMESPEED)
        
        # Uppdaterar räknare
        global_counter +=1
        removal_time -= 1
        
        if removal_time == 0:
            eaten = True
            if len(snake_x) > 0:
                snake_x.pop()
                snake_y.pop()
                score -= 1
        
        if game_over and display_endscreen: 
            show_endscreen(score)
pygame.quit()
quit()