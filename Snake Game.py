import pygame  # Импорт библиотеки Pygame
import random  # Импорт библиотеки random

# Инициализация Pygame
pygame.init()

# Константы
RES = 700  # Размер экрана
SIZE = 25  # Размер змейки и яблока

# Цвета
BLACK = (0, 0, 0)  # Черный цвет
GREEN = (0, 100, 0)  # Зеленый цвет
WHITE = (225, 225, 250)  # Белый цвет
GRAY = (14, 20, 20)  # Серый цвет
PINK = (255, 105, 136)  # Розовый цвет
BLUE = (124, 168, 250)  # Синий цвет
LIGHT_GRAY = (176, 196, 222)  # Светло-серый цвет

# Инициализация переменных
x, y = random.randrange(0, RES, SIZE), random.randrange(0, RES, SIZE)  # Координаты змейки
apple = random.randrange(0, RES, SIZE), random.randrange(0, RES, SIZE)  # Координаты яблока
snake = [(x, y)]  # Список координат частей змейки
dx, dy = 0, 0  # Направление движения змейки
fps = 7  # Скорость змейки
length = 1  # Начальная длина змейки
score = 0  # Счет

# Загрузка изображений
snake_img = pygame.image.load('snake.png')  # Загрузка изображения змейки
snake_img = pygame.transform.scale(snake_img, (300, 400))  # Масштабирование изображения змейки
fone_img = pygame.image.load('Фон.jpg')  # Загрузка фонового изображения
fone_img = pygame.transform.scale(fone_img, (700, 685))  # Масштабирование фонового изображения
obstacle_img = pygame.image.load('obstacle.png')  # Загрузка изображения препятствия
obstacle_img = pygame.transform.scale(obstacle_img, (SIZE, SIZE))  # Масштабирование изображения препятствия
apple_img = pygame.image.load('apple.png')  # Загрузка изображения яблока
apple_img = pygame.transform.scale(apple_img, (SIZE, SIZE))  # Масштабирование изображения яблока

# Настройка экрана
sc = pygame.display.set_mode([RES, RES])  # Установка размера экрана
pygame.display.set_caption('Snake Game')  # Установка заголовка окна

clock = pygame.time.Clock()  # Создание объекта для отслеживания времени
font = pygame.font.Font(None, 36)  # Установка шрифта

# Объявление препятствий
obstacles = []  # Список препятствий

# Функция для генерации нового препятствия
def generate_obstacle():
    while True:
        obstacle = (random.randrange(0, RES, SIZE), random.randrange(0, RES, SIZE))  # Генерация координат препятствия
        if obstacle not in snake and obstacle != apple:  # Проверка, чтобы препятствие не совпадало с координатами змейки и яблока
            obstacles.append(obstacle)  # Добавление препятствия в список
            break

# Генерация начальных препятствий
for _ in range(0):  # Цикл для генерации начальных препятствий
    generate_obstacle()

# Функция для отображения текста на экране
def message_to_screen(msg, color, y_displace=0):
    screen_text = font.render(msg, True, color)  # Рендеринг текста
    sc.blit(screen_text, [RES / 6, RES / 3 + y_displace])  # Отображение текста на экране

# Функция для рисования кнопок
def draw_button(msg, color, button_rect):
    pygame.draw.rect(sc, color, button_rect)  # Рисование прямоугольника кнопки
    text_surf = font.render(msg, True, BLACK)  # Рендеринг текста кнопки
    text_rect = text_surf.get_rect(center=button_rect.center)  # Центрирование текста на кнопке
    sc.blit(text_surf, text_rect)  # Отображение текста на кнопке

# Функция для сброса переменных
def reset_game():
    global x, y, dx, dy, length, snake, apple, score, obstacles
    x, y = random.randrange(0, RES, SIZE), random.randrange(0, RES, SIZE)  # Сброс координат змейки
    apple = random.randrange(0, RES, SIZE), random.randrange(0, RES, SIZE)  # Сброс координат яблока
    snake = [(x, y)]  # Сброс списка координат частей змейки
    dx, dy = 0, 0  # Сброс направления движения змейки
    length = 1  # Сброс длины змейки
    score = 0  # Сброс счета
    obstacles = []  # Сброс списка препятствий
    for _ in range(0):  # Цикл для генерации начальных препятствий
        generate_obstacle()

# Основной игровой цикл
def gameLoop():
    global x, y, dx, dy, length, snake, apple, score

    game_over = False  # Флаг окончания игры
    game_close = False  # Флаг закрытия игры
    game_start = False  # Флаг начала игры

    while not game_over:
        while not game_start:
            sc.fill(BLUE)  # Заполнение экрана розовым цветом
            sc.blit(snake_img, ((RES - snake_img.get_width()) // 2, (RES - snake_img.get_height()) // 2))  # Отображение изображения змейки
            message_to_screen("Welcome to Snake Game!", PINK, -160)  # Отображение приветственного сообщения

            # Определение кнопок
            start_button = pygame.Rect(RES // 2 - 50, RES // 2 + 100, 100, 40)  # Координаты кнопки "Start"
            quit_button = pygame.Rect(RES // 2 - 50, RES // 2 + 150, 100, 40)  # Координаты кнопки "Quit"

            # Рисование кнопок
            draw_button("Start", WHITE, start_button)  # Рисование кнопки "Start"
            draw_button("Quit", WHITE, quit_button)  # Рисование кнопки "Quit"

            pygame.display.update()  # Обновление экрана

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Проверка события выхода
                    game_over = True
                    game_start = True
                if event.type == pygame.MOUSEBUTTONDOWN:  # Проверка события нажатия кнопки мыши
                    if start_button.collidepoint(event.pos):  # Проверка нажатия кнопки "Start"
                        game_start = True
                    if quit_button.collidepoint(event.pos):  # Проверка нажатия кнопки "Quit"
                        game_over = True
                        game_start = True
                    for _ in range(0):  # Цикл для генерации начальных препятствий
                        generate_obstacle()

        while game_close:
            sc.fill(LIGHT_GRAY)  # Заполнение экрана синим цветом
            sc.blit(fone_img, ((RES - fone_img.get_width()) // 2, (RES - fone_img.get_height()) // 2))  # Отображение фонового изображения
            message_to_screen(f"Game Over! Score: {score}", GRAY)  # Отображение сообщения об окончании игры

            # Определение кнопок
            restart_button = pygame.Rect(RES // 2 - 50, RES // 2 + 50, 100, 40)  # Координаты кнопки "Restart"
            quit_button = pygame.Rect(RES // 2 - 50, RES // 2 + 100, 100, 40)  # Координаты кнопки "Quit"

            # Рисование кнопок
            draw_button("Restart", WHITE, restart_button)  # Рисование кнопки "Restart"
            draw_button("Quit", WHITE, quit_button)  # Рисование кнопки "Quit"

            pygame.display.update()  # Обновление экрана

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Проверка события выхода
                    game_over = True
                    game_close = False
                if event.type == pygame.MOUSEBUTTONDOWN:  # Проверка события нажатия кнопки мыши
                    if restart_button.collidepoint(event.pos):  # Проверка нажатия кнопки "Restart"
                        reset_game()  # Сброс игры
                        game_close = False
                    if quit_button.collidepoint(event.pos):  # Проверка нажатия кнопки "Quit"
                        game_over = True
                        game_close = False

        for event in pygame.event.get():  # Обработка всех событий Pygame
            if event.type == pygame.QUIT:  # Проверка события выхода
                game_over = True  # Установка флага окончания игры
            if event.type == pygame.KEYDOWN:  # Проверка события нажатия клавиши
                if event.key == pygame.K_w:  # Проверка нажатия клавиши "W"
                    if dy == 0:  # Проверка, что змейка не движется по вертикали
                        dx, dy = 0, -1  # Изменение направления движения на вверх
                elif event.key == pygame.K_s:  # Проверка нажатия клавиши "S"
                    if dy == 0:  # Проверка, что змейка не движется по вертикали
                        dx, dy = 0, 1  # Изменение направления движения на вниз
                elif event.key == pygame.K_a:  # Проверка нажатия клавиши "A"
                    if dx == 0:  # Проверка, что змейка не движется по горизонтали
                        dx, dy = -1, 0  # Изменение направления движения на влево
                elif event.key == pygame.K_d:  # Проверка нажатия клавиши "D"
                    if dx == 0:  # Проверка, что змейка не движется по горизонтали
                        dx, dy = 1, 0  # Изменение направления движения на вправо

        x += dx * SIZE  # Обновление координаты x змейки
        y += dy * SIZE  # Обновление координаты y змейки

        # Проверка столкновений с экраном
        if x >= RES or x < 0 or y >= RES or y < 0:  # Проверка выхода за границы экрана
            game_close = True  # Установка флага окончания игры

        snake_head = (x, y)  # Обновление координат головы змейки
        snake.append(snake_head)  # Добавление головы змейки в список частей змейки

        # Проверка съест ли змея яблоко
        if snake_head == apple:  # Проверка совпадения координат головы змейки и яблока
            apple = random.randrange(0, RES, SIZE), random.randrange(0, RES, SIZE)  # Генерация новых координат яблока
            length += 1  # Увеличение длины змейки
            score += 1  # Увеличение счета
            obstacles.clear()  # Очистка списка препятствий
            for _ in range(5):  # Генерация 5 препятствий при счете >= 5
                if score >= 5:
                    generate_obstacle()
            for _ in range(10):  # Генерация 10 препятствий при счете >= 10
                if score >= 10:
                    generate_obstacle()
            for _ in range(15):  # Генерация 15 препятствий при счете >= 15
                if score >= 15:
                    generate_obstacle()
            for _ in range(20):  # Генерация 20 препятствий при счете >= 20
                if score >= 20:
                    generate_obstacle()
            for _ in range(25):  # Генерация 25 препятствий при счете >= 25
                if score >= 25:
                    generate_obstacle()
            for _ in range(30):  # Генерация 30 препятствий при счете >= 30
                if score >= 30:
                    generate_obstacle()
        else:
            snake = snake[1:]  # Удаление последней части змейки, если яблоко не съедено

        # Проверка столкновения змеи с самой собой
        if len(snake) != len(set(snake)):  # Проверка на совпадение координат частей змейки
            game_close = True  # Установка флага окончания игры

        # Проверка столкновения змеи с препятствиями
        if snake_head in obstacles:  # Проверка на совпадение координат головы змейки и препятствий
            game_close = True  # Установка флага окончания игры

        sc.fill(BLACK)  # Заполнение экрана черным цветом
        sc.blit(apple_img, apple)  # Отображение изображения яблока

        for i, j in snake:  # Отображение всех частей змейки
            pygame.draw.rect(sc, GREEN, (i + 1, j + 1, SIZE - 2, SIZE - 2))  # Рисование части змейки

        for obstacle in obstacles:  # Отображение всех препятствий
            sc.blit(obstacle_img, obstacle)  # Рисование изображения препятствия

        score_text = font.render(f'Score: {score}', True, (255, 255, 255))  # Рендеринг текста счета
        sc.blit(score_text, (10, 10))  # Отображение текста счета на экране

        pygame.display.update()  # Обновление экрана

        clock.tick(fps)  # Установка скорости игры

    pygame.quit()  # Завершение работы Pygame
    quit()  # Завершение работы программы

gameLoop()  # Запуск основной игровой функции
