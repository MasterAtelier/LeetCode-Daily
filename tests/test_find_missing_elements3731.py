from    problems.find_missing_elements3731 import Solution

def test_example1():
    nums = [1,4,2,5]
    assert Solution().findMissingElements(nums) == [3]
def test_example2():
    nums = [7,8,6,9]
    assert Solution().findMissingElements(nums) == []

def test_example3():
    nums = [1, 5]
    assert Solution().findMissingElements(nums) == [2,3,4]