

from problems.find_the_minimum_and_maximum_number_of_nodes_between_critical_points2058 import Solution
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def test_example1():

    head = build_list([5, 3, 1, 2, 5, 1, 2])

    assert Solution().nodesBetweenCriticalPoints(head) == [1, 3]


def test_example2():

    head = build_list([1, 3, 2, 2, 3, 2, 2, 2, 7])

    assert Solution().nodesBetweenCriticalPoints(head) == [3, 3]


def test_no_critical_points():

    head = build_list([1, 2, 3, 4, 5])

    assert Solution().nodesBetweenCriticalPoints(head) == [-1, -1]


def test_only_one_critical_point():

    head = build_list([1, 3, 2, 4])

    assert Solution().nodesBetweenCriticalPoints(head) == [1, 1]


def test_exactly_two_critical_points():

    head = build_list([1, 3, 1, 2])

    assert Solution().nodesBetweenCriticalPoints(head) == [1, 1]


def test_multiple_critical_points():

    head = build_list([1, 5, 2, 4, 1, 3, 2])

    assert Solution().nodesBetweenCriticalPoints(head) == [1, 4]