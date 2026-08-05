from problems.remove_methods_from_projects3310 import Solution

def test_example1():
    n = 4
    k = 1
    invocations = [[1,2],[0,1],[3,2]]
    assert Solution().remainingMethods(n , k, invocations) == [0,1,2,3]

def test_example2():
    n = 5
    k = 0
    invocations = [[1,2],[0,2],[0,1],[3,4]]
    assert Solution().remainingMethods(n , k, invocations) == [3, 4]

def test_example3():
    n = 3
    k = 2
    invocations = [[1,2],[0,1],[2,0]]
    assert Solution().remainingMethods(n , k, invocations) == []