import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
RES = 800  # Размер экрана
SIZE = 30  # Размер змейки и яблока

# Цвета
BLACK = (0, 114, 255)
GREEN = (54, 184, 154)
LIGHT_GREEN = (225, 225, 250)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
PINK = (145, 192, 203)
BLUE = (75, 47, 147)

# Инициализация переменных
x, y = random.randrange(0, RES, SIZE), random.randrange(0, RES, SIZE)
apple = random.randrange(0, RES, SIZE), random.randrange(0, RES, SIZE)
snake = [(x, y)]
dx, dy = 0, 0
fps = 7  # Скорость змейки
length = 1  # Начальная длина змейки

# Загрузка изображения
snake_img = pygame.image.load('snake.png')
snake_img = pygame.transform.scale(snake_img, (300, 400))

# Настройка экрана
sc = pygame.display.set_mode([RES, RES])
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)


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
    global x, y, dx, dy, length, snake, apple
    x, y = random.randrange(0, RES, SIZE), random.randrange(0, RES, SIZE)
    apple = random.randrange(0, RES, SIZE), random.randrange(0, RES, SIZE)
    snake = [(x, y)]
    dx, dy = 0, 0
    length = 1


# Основной игровой цикл
def gameLoop():
    global x, y, dx, dy, length, snake, apple

    game_over = False
    game_close = False
    game_start = False

    while not game_over:
        while not game_start:
            sc.fill(PINK)
            sc.blit(snake_img, ((RES - snake_img.get_width()) // 2, (RES - snake_img.get_height()) // 2))
            message_to_screen("Welcome to Snake Game!", WHITE, -150)

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

        while game_close:
            sc.fill(BLUE)
            message_to_screen("Game Over!", RED)

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
        else:
            snake = snake[1:]

        # Проверка столкновения змеи с самой собой
        if len(snake) != len(set(snake)):
            game_close = True

        # Рисование всего на экране
        sc.fill(BLACK)
        pygame.draw.rect(sc, RED, (*apple, SIZE, SIZE))

        for i, j in snake:
            pygame.draw.rect(sc, GREEN, (i + 1, j + 1, SIZE - 2, SIZE - 2))

        pygame.display.update()

        # Контроль скорости игры
        clock.tick(fps)

    pygame.quit()
    quit()


gameLoop()

