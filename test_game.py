from game import Game

def test_game():
    game = Game('test_game.txt')
    game.setStart()
    assert [game.player.row, game.player.col] == [0, 2], 'Method setStart failed'
    print('test1 passed: Method setStart')

    assert game.row == 4, 'game.row failed'
    print('test2 passed: game.row passed')
    assert game.column == 6, 'game.column failed'
    print('test3 passed: game.column passed')

    """Positive test cases"""
    #  step into air
    game.coordinateUpdate('s', game)
    new = game.showGrid()
    assert game.moves == ['s'], 'game.moves failed'
    assert game.movesNum == 1, 'game.movesNum failed'
    print('test4 passed: game attributes are correct')
    assert new == '**X***\n' \
                  '*1A  *\n' \
                  '*W F1*\n' \
                  '*  Y**\n\n' \
                  'You have 0 water buckets.', 'Step into Air failed'
    print('test5 passed: Step into Air')

    #  step into teleport
    game.coordinateUpdate('a', game)
    new = game.showGrid()
    assert game.moves == ['s', 'a'], 'game.moves failed'
    assert game.movesNum == 2, 'game.movesNum failed'
    print('test6 passed: game attributes are correct')
    assert new == '**X***\n' \
                  '*1   *\n' \
                  '*W FA*\n' \
                  '*  Y**\n\n' \
                  'You have 0 water buckets.', 'Step into Teleport failed'
    print('test7 passed: Step into Teleport')

    #  step into water
    for move in ['w', 'a', 'a', 's', 'a']:
        game.coordinateUpdate(move, game)
    new = game.showGrid()
    assert game.moves == ['s', 'a', 'w', 'a', 'a', 's', 'a'], 'game.moves failed'
    assert game.movesNum == 7, 'game.movesNum failed'
    print('test8 passed: game attributes are correct')
    assert new == '**X***\n' \
                  '*1   *\n' \
                  '*A F1*\n' \
                  '*  Y**\n\n' \
                  'You have 1 water bucket.', 'Step into Water failed'
    print('test9 passed: Step into Water')

    #  step into fire with water
    for move in ['d', 'd']:
        game.coordinateUpdate(move, game)
    new = game.showGrid()
    assert game.moves == ['s', 'a', 'w', 'a', 'a', 's', 'a', 'd', 'd'], 'game.moves failed'
    assert game.movesNum == 9, 'game.movesNum failed'
    print('test10 passed: game attributes are correct')
    assert new == '**X***\n' \
                  '*1   *\n' \
                  '*  A1*\n' \
                  '*  Y**\n\n' \
                  'You have 0 water buckets.', 'Step into Fire with water failed'
    print('test11 passed: Step into Fire with water passed')

    #  reach the end successfully
    game.coordinateUpdate('s', game)
    new = game.showGrid()
    assert game.moves == ['s', 'a', 'w', 'a', 'a', 's', 'a', 'd', 'd', 's'], 'game.moves failed'
    assert game.movesNum == 10, 'game.movesNum failed'
    print('test12 passed: game attributes are correct')
    assert new == '**X***\n' \
                  '*1   *\n' \
                  '*   1*\n' \
                  '*  A**\n\n' \
                  'You have 0 water buckets.', 'Step into End failed'
    print('test13 passed: Step into End')

    #  step into fire without water
    game2 = Game('test_game.txt')
    game2.setStart()
    for move in ['s', 'd', 's']:
        game2.coordinateUpdate(move, game2)
    new = game2.showGrid()
    assert game2.moves == ['s', 'd', 's'], 'game.moves failed'
    assert game2.movesNum == 3, 'game.movesNum failed'
    print('test14 passed: game attributes are correct')
    assert new == '**X***\n' \
                  '*1   *\n' \
                  '*W A1*\n' \
                  '*  Y**\n\n' \
                  'You have 0 water buckets.', 'Step into Fire without water failed'
    print('test15 passed: Step into Fire without water')

    #  test command 'e'
    game = Game('test_game.txt')
    game.setStart()
    for move in ['s', 'e']:
        game.coordinateUpdate(move, game)
    new = game.showGrid()
    assert game.moves == ['s', 'e'], 'game.moves failed'
    assert game.movesNum == 2, 'game.movesNum failed'
    print('test16 passed: game attributes are correct')
    assert new == '**X***\n' \
                  '*1A  *\n' \
                  '*W F1*\n' \
                  '*  Y**\n\n' \
                  'You have 0 water buckets.', "Command 'e' failed"
    print("test17 passed: Command 'e' passed")

    #  test command 'q'
    game.coordinateUpdate('q', game)
    new = game.showGrid()
    assert game.moves == ['s', 'e'], 'game.moves failed'
    assert game.movesNum == 2, 'game.movesNum failed'
    print('test18 passed: game attributes are correct')
    assert new == '**X***\n' \
                  '*1A  *\n' \
                  '*W F1*\n' \
                  '*  Y**\n\n' \
                  'You have 0 water buckets.', "Command 'q' failed"
    print("test19 passed: Command 'q' passed")

    #  test uppercase
    #  these should be still uppercase, because I turned them into lowercase when using cell.step()
    for move in ['D']:
        game.coordinateUpdate(move, game)
    new = game.showGrid()
    assert game.moves == ['s', 'e', 'D'], 'game.moves failed'
    assert game.movesNum == 3, 'game.movesNum failed'
    print('test20 passed: game attributes are correct')
    assert new == '**X***\n' \
                  '*1 A *\n' \
                  '*W F1*\n' \
                  '*  Y**\n\n' \
                  'You have 0 water buckets.', "uppercase failed"
    print("test21 passed: uppercase passed")
    print('positive tests all passed')

    """Negative cases"""
    #  invalid input
    game.coordinateUpdate('asc', game)
    new = game.showGrid()
    assert game.moves == ['s', 'e', 'D'], 'game.moves failed'
    assert game.movesNum == 3, 'game.movesNum failed'
    print('test22 passed: game attributes are correct')
    assert new == '**X***\n' \
                  '*1 A *\n' \
                  '*W F1*\n' \
                  '*  Y**\n\n' \
                  'You have 0 water buckets.', "invalid input failed"
    print("test23 passed: invalid input passed")
    print('negative tests all passed')

    """Edge case"""
    #  go beyond the map
    for move in ['a', 's', 's', 's']:
        game.coordinateUpdate(move, game)
    new = game.showGrid()
    assert game.moves == ['s', 'e', 'D', 'a', 's', 's'], 'game.moves failed'
    assert game.movesNum == 6, 'game.movesNum failed'
    print('test24 passed: game attributes are correct')
    assert new == '**X***\n' \
                  '*1   *\n' \
                  '*W F1*\n' \
                  '* AY**\n\n' \
                  'You have 0 water buckets.', "go beyond the map failed"
    print("test25 passed: go beyond the map passed")
    print('edge tests all passed')

def run_tests():
    test_game()
    print('test_game all passed \n')
