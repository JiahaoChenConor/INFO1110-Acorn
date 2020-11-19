from game_parser import parse
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)


def test_parse():
    """Positive test"""
    lines1 = ['**X**',
              '*1 1*',
              '**Y**']
    grid = parse(lines1)
    for i in range(3):
        for j in range(5):

            if i == 0 and j == 2:
                assert isinstance(grid[i][j], Start), 'test1 Start failed'
            elif (i == 1 and j == 1) or (i == 1 and j == 3):
                assert isinstance(grid[i][j], Teleport), 'test1 Teleport failed'
                assert grid[i][j].display == 1, 'test1 Teleport failed'
            elif i == 2 and j == 2:
                assert isinstance(grid[i][j], End), 'test1 End failed'
            elif i == 1 and j == 2:
                assert isinstance(grid[i][j], Air), 'test1 Air failed'
            else:
                assert isinstance(grid[i][j], Wall), 'test1 Wall failed'
    print('test1 passed')
    print('postive tests all passed')



    """Negative tests"""
    #  without Start
    lines2 = ['***',
              '* *',
              '*Y*']
    excepted = ValueError("Expected 1 starting position, got 0.")
    try:
        parse(lines2)
    except ValueError as e:
        assert str(excepted) == str(e), 'test2 failed.'
    print('test2 passed')

    #  two instances of End class
    lines3 = ['*X*',
              '* *',
              '*YY']
    excepted = ValueError("Expected 1 ending position, got 2.")
    try:
        parse(lines3)
    except ValueError as e:
        assert str(excepted) == str(e), 'test3 failed.'
    print('test3 passed')

    #  display of teleport is not in 1-9
    lines4 = ['**X**',
              '*0 0*',
              '**Y**']
    excepted = ValueError('Bad letter in configuration file: 0.')
    try:
        parse(lines4)
    except ValueError as e:
        assert str(excepted) == str(e), 'test4 failed.'
    print('test4 passed')

    #  teleports don't come in pairs
    lines5 = ['**X**',
              '*1 1*',
              '*1  *',
              '**Y**']
    excepted = ValueError("Teleport pad 1 does not have an exclusively matching pad.")
    try:
        parse(lines5)
    except ValueError as e:
        assert str(excepted) == str(e), 'test5 failed.'
    print('test5 passed')
    print('negative tests all paseed')


    """Edge tests"""
    #  if empty file,it will raise the first error(Zero staring position).
    lines6 = []
    excepted = ValueError("Expected 1 starting position, got 0.")
    try:
        parse(lines6)
    except ValueError as e:
        assert str(excepted) == str(e), 'test6 failed.'
    print('test6 passed')

    #  not all element in list are string
    line7 = ['**X*',
              1122,
             '**Y*']
    excepted = AttributeError("'int' object has no attribute 'strip'")
    try:
        parse(line7)
    except AttributeError as e:
        assert str(excepted) == str(e), 'test7 failed'
    print('test7 passed')
    print('edge tests all passed')

def run_tests():
    test_parse()
    print('test_parse all passed\n')


