import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
RES = 700  # Размер экрана
SIZE = 25  # Размер змейки и яблока

# Цвета
BLACK = (0, 0, 0)
GREEN = (0, 100, 0)
LIGHT_GREEN = (225, 225, 250)
RED = (220, 20, 20)
WHITE = (255, 105, 136)
PINK = (230, 230, 250)
BLUE = (176, 196, 222)

# Инициализация переменных
x, y = random.randrange(0, RES, SIZE), random.randrange(0, RES, SIZE)
apple = random.randrange(0, RES, SIZE), random.randrange(0, RES, SIZE)
snake = [(x, y)]
dx, dy = 0, 0
fps = 7  # Скорость змейки
length = 1  # Начальная длина змейки
score = 0  # Счет

# Загрузка изображений
snake_img = pygame.image.load('snake.png')
snake_img = pygame.transform.scale(snake_img, (300, 400))
fone_img = pygame.image.load('Фон.jpg')
fone_img = pygame.transform.scale(fone_img, (700, 685))
obstacle_img = pygame.image.load('obstacle.png')
obstacle_img = pygame.transform.scale(obstacle_img, (SIZE, SIZE))
apple_img = pygame.image.load('apple.png')
apple_img = pygame.transform.scale(apple_img, (SIZE, SIZE))

# Настройка экрана
sc = pygame.display.set_mode([RES, RES])
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Объявление препятствий
obstacles = []

# Функция для генерации нового препятствия
def generate_obstacle():
    while True:
        obstacle = (random.randrange(0, RES, SIZE), random.randrange(0, RES, SIZE))
        if obstacle not in snake and obstacle != apple:
            obstacles.append(obstacle)
            break

# Генерация начальных препятствий
for _ in range(0):
    generate_obstacle()

# Функция для отображения текста на экране
def message_to_screen(msg, color, y_displace=0):
    screen_text = font.render(msg, True, color)
    sc.blit(screen_text, [RES / 6, RES / 3 + y_displace])

# Функция для рисования кнопок
def draw_button(msg, color, button_rect):
    pygame.draw.rect(sc, color, button_rect)
    text_surf = font.render(msg, True, BLACK)
    text_rect = text_surf.get_rect(center=button_rect.center)
    sc.blit(text_surf, text_rect)

# Функция для сброса переменных
def reset_game():
    global x, y, dx, dy, length, snake, apple, score, obstacles
    x, y = random.randrange(0, RES, SIZE), random.randrange(0, RES, SIZE)
    apple = random.randrange(0, RES, SIZE), random.randrange(0, RES, SIZE)
    snake = [(x, y)]
    dx, dy = 0, 0
    length = 1
    score = 0  # Сброс счета
    obstacles = []
    for _ in range(0):
        generate_obstacle()

# Основной игровой цикл
def gameLoop():
    global x, y, dx, dy, length, snake, apple, score

    game_over = False
    game_close = False
    game_start = False

    while not game_over:
        while not game_start:
            sc.fill(PINK)
            sc.blit(snake_img, ((RES - snake_img.get_width()) // 2, (RES - snake_img.get_height()) // 2))
            message_to_screen("Welcome to Snake Game!", WHITE, -160)

            # Определение кнопок
            start_button = pygame.Rect(RES // 2 - 50, RES // 2 + 100, 100, 40)
            quit_button = pygame.Rect(RES // 2 - 50, RES // 2 + 150, 100, 40)

            # Рисование кнопок
            draw_button("Start", LIGHT_GREEN, start_button)
            draw_button("Quit", LIGHT_GREEN, quit_button)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_start = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.collidepoint(event.pos):
                        game_start = True
                    if quit_button.collidepoint(event.pos):
                        game_over = True
                        game_start = True
                    for _ in range(0):
                        generate_obstacle()

        while game_close:
            sc.fill(BLUE)
            sc.blit(fone_img, ((RES - fone_img.get_width()) // 2, (RES - fone_img.get_height()) // 2))
            message_to_screen(f"Game Over! Score: {score}", RED)

            # Определение кнопок
            restart_button = pygame.Rect(RES // 2 - 50, RES // 2 + 50, 100, 40)
            quit_button = pygame.Rect(RES // 2 - 50, RES // 2 + 100, 100, 40)

            # Рисование кнопок
            draw_button("Restart", PINK, restart_button)
            draw_button("Quit", PINK, quit_button)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_button.collidepoint(event.pos):
                        reset_game()
                        game_close = False
                    if quit_button.collidepoint(event.pos):
                        game_over = True
                        game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if dy == 0:
                        dx, dy = 0, -1
                elif event.key == pygame.K_s:
                    if dy == 0:
                        dx, dy = 0, 1
                elif event.key == pygame.K_a:
                    if dx == 0:
                        dx, dy = -1, 0
                elif event.key == pygame.K_d:
                    if dx == 0:
                        dx, dy = 1, 0

        x += dx * SIZE
        y += dy * SIZE

        # Проверка столкновений с экраном
        if x >= RES or x < 0 or y >= RES or y < 0:
            game_close = True

        snake_head = (x, y)
        snake.append(snake_head)

        # Проверка съест ли змея яблоко
        if snake_head == apple:
            apple = random.randrange(0, RES, SIZE), random.randrange(0, RES, SIZE)
            length += 1
            score += 1  # Увеличение счета
            obstacles.clear()
            for _ in range(5):
                if score >= 5:
                    generate_obstacle()
            for _ in range(10):
                if score >= 10:
                    generate_obstacle()
            for _ in range(15):
                if score >= 15:
                    generate_obstacle()
            for _ in range(20):
                if score >= 20:
                    generate_obstacle()
            for _ in range(25):
                if score >= 25:
                    generate_obstacle()
            for _ in range(30):
                if score >= 30:
                    generate_obstacle()
        else:
            snake = snake[1:]

        # Проверка столкновения змеи с самой собой
        if len(snake) != len(set(snake)):
            game_close = True

        # Проверка столкновения змеи с препятствиями
        if snake_head in obstacles:
            game_close = True

        # Рисование всего на экране
        sc.fill(BLACK)
        sc.blit(apple_img, apple)

        for i, j in snake:
            pygame.draw.rect(sc, GREEN, (i + 1, j + 1, SIZE - 2, SIZE - 2))

        for obstacle in obstacles:
            sc.blit(obstacle_img, obstacle)

        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        sc.blit(score_text, (10, 10))

        pygame.display.update()

        # Контроль скорости игры
        clock.tick(fps)

    pygame.quit()
    quit()

gameLoop()
