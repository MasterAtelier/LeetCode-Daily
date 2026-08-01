from problems.predict_the_winner486 import Solution

def test_example1():
    nums = [1,5,2]
    assert Solution().predictTheWinner(nums) == False

def test_example2():
    nums = [1,5,233,7]
    assert Solution().predictTheWinner(nums) == True