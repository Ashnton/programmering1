#Uppgift 9
#Nedan är ett kod för pong. Dock saknas kod för att få bollen att ändra riktning vid väggarna
#och paddlarna. SE "Ball collision with paddles" rad 75 och "# Ball collision with walls" rad 69
#
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 8

# Ball settings
BALL_SIZE = 15
BALL_SPEED_X = 4
BALL_SPEED_Y = 4

# Create paddles
player1 = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Create ball
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Ball direction
ball_dx = BALL_SPEED_X
ball_dy = BALL_SPEED_Y

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Player 1 controls
    if keys[pygame.K_w]:
        player1.y -= PADDLE_SPEED
    if keys[pygame.K_s]:
        player1.y += PADDLE_SPEED

    # Player 2 controls
    percentage_chance = 0.05
    
    # if keys[pygame.K_UP]:
    if (ball.y < player2.y):
        if random.random() < percentage_chance:
            player2.y += PADDLE_SPEED
    
        player2.y -= PADDLE_SPEED
    # if keys[pygame.K_DOWN]:
    if (ball.y > player2.y):
        if random.random() < percentage_chance:
            player2.y -= PADDLE_SPEED
    
        player2.y += PADDLE_SPEED

    # Ball movement
    ball.x += ball_dx
    ball.y += ball_dy

    # Ball collision with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *=-1
    # walls är uppe och nere på skärmen och paddles är höger och vänster sida.

    # Ball collision with paddles
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_dx *=-1
    # Ball out of bounds
    if ball.left <= 0 or ball.right >= WIDTH:
        # Reset ball position
        ball.center = (WIDTH // 2, HEIGHT // 2)
        # Reset ball direction
        ball_dx *= -1

    # Clear the screen
    screen.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)