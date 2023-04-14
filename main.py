import pygame
import random
import sys

pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Определение размера экрана
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Определение шрифта
font = pygame.font.SysFont(None, 25)

# Определение гравитации и скорости
gravity = 0.5
bird_movement = 0

# Определение труб
pipe_gap = 150
pipe_width = 50
min_pipe_height = 100  # Минимальная высота трубы, при которой она будет отображаться на экране полностью
pipe_height = random.randint(min_pipe_height, SCREEN_HEIGHT - pipe_gap - min_pipe_height)
pipe_x = SCREEN_WIDTH
pipe_y = random.randint(-pipe_height//2, SCREEN_HEIGHT-pipe_gap-pipe_height//2)
lower_pipe_y = pipe_height + pipe_gap  # Координата нижнего края верхней трубы


# Определение птицы
bird_x = 50
bird_y = SCREEN_HEIGHT // 2
bird_width = 30
bird_height = 30

# Определение функций
def draw_bird():
    pygame.draw.rect(screen, BLUE, (bird_x, bird_y, bird_width, bird_height))

def move_pipes():
    global pipe_x, pipe_y, pipe_height
    pipe_x -= 2
    if pipe_x < -pipe_width:
        pipe_x = SCREEN_WIDTH
        pipe_height = random.randint(150, 350)
        pipe_y = random.randint(-pipe_height//2, SCREEN_HEIGHT-pipe_gap-pipe_height//2)

def draw_pipes():
    global pipe_x, pipe_y, pipe_height
    if pipe_y < 0:
        pipe_height += pipe_y
        pipe_y = 0
    pygame.draw.rect(screen, GREEN, (pipe_x, pipe_y, pipe_width, int(pipe_height)))
    pygame.draw.rect(screen, GREEN, (pipe_x, pipe_y+int(pipe_height)+pipe_gap, pipe_width, SCREEN_HEIGHT-int(pipe_height)-pipe_gap))


def display_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, [10, 10])

def check_collision():
    if bird_y < 0 or bird_y > SCREEN_HEIGHT - bird_height:
        return True
    if pipe_x <= bird_x + bird_width <= pipe_x + pipe_width and (bird_y <= pipe_y + pipe_height or bird_y + bird_height >= pipe_y + pipe_height + pipe_gap):
        return True
    return False

# Главный игровой цикл
score = 0
game_over = False
clock = pygame.time.Clock()
while not game_over:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = -7

    # Движение птицы
    bird_movement += gravity
    bird_y += bird_movement

    # Движение труб
    move_pipes()

    # Рисование объектов
    screen.fill(BLACK)
    draw_bird()
    draw_pipes()
    display_score(score)

    # Проверка столкновений
    if check_collision():
        game_over = True

    # Проверка прохождения
    if pipe_x == bird_x - pipe_width:
        score += 1

    # Обновление экрана
    pygame.display.update()

    # Задержка
    clock.tick(60)

