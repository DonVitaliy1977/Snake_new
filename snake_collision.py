from snake import Snake

from constans import WIDTH, HEIGHT


def wall_collision(snake: Snake):
    x, y = snake.head.x, snake.head.y
    if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
        snake.alive = False
