from grid import grid_to_string
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)
from player import Player


def test_grid():
    """Positive test"""
    #  one bucket
    t1, t2 = Teleport(), Teleport()
    t1.display, t2.display = 1, 1
    grid = [[Wall(), Wall(), Start(), Wall(), Wall()],
            [Wall(), Water(), Air(), t1, Wall()],
            [Wall(), t2, Air(), Air(), Wall()],
            [Wall(), Wall(), End(), Wall(), Wall()]]

    player = Player()
    player.row = 1
    player.col = 1
    player.num_water_buckets = 1
    excepted = '**X**\n' \
               '*A 1*\n' \
               '*1  *\n' \
               '**Y**\n\n' \
               'You have 1 water bucket.'
    assert grid_to_string(grid, player) == excepted, 'test1 failed'
    print('test1 passed')

    #  more than one bucket
    player.num_water_buckets = 2
    excepted = '**X**\n' \
               '*A 1*\n' \
               '*1  *\n' \
               '**Y**\n\n' \
               'You have 2 water buckets.'
    assert grid_to_string(grid, player) == excepted, 'test2 failed'
    print('test2 passed')
    print("positive tests all passed")

    """Negative test"""
    #  gird is not a list
    grid = 'a'
    excepted = IndexError("string index out of range")
    try:
        grid_to_string(grid, player)
    except IndexError as e:
        assert str(excepted) == str(e), 'test2 failed'
    except Exception:
        print('test3 failed')
    print('test3 passed')

    #  player is not the object of Player
    grid = [[Wall(), Wall(), Start(), Wall(), Wall()],
            [Wall(), Water(), Air(), t1, Wall()],
            [Wall(), t2, Air(), Air(), Wall()],
            [Wall(), Wall(), End(), Wall(), Wall()]]
    excepted = AttributeError("'str' object has no attribute 'row'")
    try:
        grid_to_string(grid, 'a')
    except AttributeError as e:
        assert str(excepted) == str(e), 'test4 failed'
    except Exception:
        print('test4 failed')
    print('test4 passed')
    print("negative tests all passed")

    """Edge case"""
    #  grid is list, but one of its element is not object of cell
    grid = [[' ', Wall(), Start(), Wall(), Wall()],
            [Wall(), Water(), Air(), t1, Wall()],
            [Wall(), t2, Air(), Air(), Wall()],
            [Wall(), Wall(), End(), Wall(), Wall()]]
    excepted = AttributeError("'str' object has no attribute 'display'")
    try:
        grid_to_string(grid, player)
    except AttributeError as e:
        assert str(excepted) == str(e), 'test5 failed'
    except Exception:
        print('test5 failed')
    print('test5 passed')

    #  grid is empty
    grid = []
    excepted = IndexError("list index out of range")
    try:
        grid_to_string(grid, player)
    except IndexError as e:
        assert str(excepted) == str(e), 'test6 failed'
    except Exception:
        print('test6 failed')
    print('test6 passed')
    print('edge tests all passed')


def run_tests():
    test_grid()
    print("test_grid all passed\n")




