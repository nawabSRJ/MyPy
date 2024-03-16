import pygame
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define screen dimensions
WIDTH = 800
HEIGHT = 600

# Define block size
BLOCK_SIZE = 20

# Define snake speed
SNAKE_SPEED = 10

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Define the font
font = pygame.font.SysFont(None, 25)

# Define functions
def start_snake():
    x = WIDTH // 2
    y = HEIGHT // 2
    return [(x, y), (x - BLOCK_SIZE, y), (x - 2 * BLOCK_SIZE, y)]

def spawn_food():
    return [random.randrange(0, WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
            random.randrange(0, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE]

def draw_snake(snake):
    for block in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))

def display_score(score):
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, [0, 0])

def is_collision(snake):
    head = snake[-1]
    return head in snake[:-1] or head[0] < 0 or head[0] > WIDTH - BLOCK_SIZE or head[1] < 0 or head[1] > HEIGHT - BLOCK_SIZE

def game_loop():
    game_over = False
    snake = start_snake()
    food = spawn_food()
    score = 0

    x1_change = 0
    x2_change = 0
    y1_change = 0
    y2_change = 0

    clock = pygame.time.Clock()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change != BLOCK_SIZE:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change != -BLOCK_SIZE:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change != BLOCK_SIZE:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change != -BLOCK_SIZE:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

        # Update snake position
        x = snake[-1][0] + x1_change
        y = snake[-1][1] + y1_change
        head = [x, y]
        snake.append(head)
        snake.pop(0)

        # Check for collision with food
        if head == food:
            food = spawn_food()
            score += 1

        # Check for collision
        if is_collision(snake):
            game_over = True

        # Clear the screen
        screen.fill(BLACK)

        # Draw the snake and food
        draw_snake(snake)
        draw_food(food)
        display_score(score)

        # Update the display
        pygame.display.flip()

        # Control game speed
        clock.tick(SNAKE_SPEED)

# Start the game
game_loop()

# Quit Pygame
pygame.quit()
