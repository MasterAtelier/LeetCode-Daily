from problems.stone_game_III1406 import Solution

def test_example1():
    stoneValue = [1,2,3,7]
    assert Solution().stoneGameIII(stoneValue) == "Bob"

def test_example2():
    stoneValue = [1,2,3,-9]
    assert Solution().stoneGameIII(stoneValue) == "Alice"

def test_example3():
    stoneValue = [1,2,3,6]
    assert Solution().stoneGameIII(stoneValue) == "Tie"

def test_example4():
    stoneValue = [1,2,3,-1,-2,-3,7]
    assert Solution().stoneGameIII(stoneValue) == "Alice"