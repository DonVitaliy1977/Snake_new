import pytest
from runner import speed_game
from snake import Snake


@pytest.fixture(scope='function')
def snake(request):
    return Snake(request.param)

# def speed_game(snake: Snake, snake_speed_limit):
#     if len(snake.tail) == 4:
#         snake_speed_limit = 30
#     elif len(snake.tail) == 9:
#         snake_speed_limit = 20
#     elif len(snake.tail) == 19:
#         snake_speed_limit = 15
#     elif len(snake.tail) > 28:
#         snake_speed_limit = 10
#     return snake_speed_limit


@pytest.mark.parametrize(
    ('snake', 'tail', 'result'),[((100, 100), [{"x": 300, "y": 120}, {"x": 330, "y": 120}], 40),
                                 ((100, 100),[{"x": 300, "y": 120},{"x": 300, "y": 120},{"x": 300, "y": 120},
                                              {"x": 330, "y": 120}], 30)], indirect=['snake']
)
def test_speed_game(snake, tail, result):
    snake.tail = tail
    assert speed_game(snake) == result

