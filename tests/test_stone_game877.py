from problems.stone_game877 import Solution

def test_example1():
    piles = [5,3,4,5]
    assert Solution().stoneGame(piles) == True

def test_example2():
    piles = [3,7,2,3]
    assert Solution().stoneGame(piles) == True