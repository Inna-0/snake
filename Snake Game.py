import pygame

FRAME_COLOR = (0, 235, 200)
WHITE = (255, 255, 255)
SIZE_BLOCK = 20
COUNT_BLOCKS = 20
BLUE = (204, 204, 255)
MARGIN = 1  # Отступ между квадратиками
HEADER_MARGIN = 70
HEADER_COLOR = (0, 204, 153)
SNAKE_COLOR = (0, 102, 0)
size = [SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS,
        SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * SIZE_BLOCK + HEADER_MARGIN]

print(size)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Змейка')  # Заголовок
timer = pygame.time.Clock()

class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def draw_block(color, row, column):
    pygame.draw.rect(screen, color, [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
                                     HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1),
                                     SIZE_BLOCK,
                                     SIZE_BLOCK])

snake_blocks = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)]

d_row = 0
d_col = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('exit')
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and d_col!=0:
                d_row = -1
                d_col = 0
            elif event.key == pygame.K_DOWN and d_col != 0:
                d_row = 1
                d_col = 0
            elif event.key == pygame.K_LEFT and d_col != 0:
                d_row = 0
                d_col = -1
            elif event.key == pygame.K_RIGHT and d_col != 0:
                d_row = 0
                d_col = 1

    screen.fill(FRAME_COLOR)  # Заливка экрана основным цветом
    pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])

    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column) % 2 == 0:
                color = BLUE
            else:
                color = WHITE

            draw_block(color, row, column)

    for block in snake_blocks:
        draw_block(SNAKE_COLOR, block.x, block.y)

    head = snake_blocks[-1]
    new_head = SnakeBlock(head.x + d_row, head.y + d_col)
    snake_blocks.append((new_head))
    snake_blocks.pop(0)
    pygame.display.flip()
    timer.tick(2)
