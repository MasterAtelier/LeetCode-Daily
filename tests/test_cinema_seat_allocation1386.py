from problems.cinema_seat_allocation1386 import Solution


def test_example1():
    n = 3
    reservedSeats = [[1, 2], [1, 3], [1, 8], [2, 6], [2, 7], [2, 9]]

    assert Solution().maxNumberOfFamilies(n, reservedSeats) == 4


def test_example2():
    n = 2
    reservedSeats = [[2, 1], [1, 8], [2, 6]]

    assert Solution().maxNumberOfFamilies(n, reservedSeats) == 2


def test_example3():
    n = 4
    reservedSeats = [[4, 2], [1, 3], [1, 8], [2, 6]]

    assert Solution().maxNumberOfFamilies(n, reservedSeats) == 5


def test_no_reserved_seats():
    n = 3
    reservedSeats = []

    assert Solution().maxNumberOfFamilies(n, reservedSeats) == 6


def test_left_and_right_groups_available():
    n = 1
    reservedSeats = [[1, 1], [1, 10]]

    assert Solution().maxNumberOfFamilies(n, reservedSeats) == 2


def test_only_middle_group_available():
    n = 1
    reservedSeats = [[1, 2], [1, 8]]

    assert Solution().maxNumberOfFamilies(n, reservedSeats) == 1


def test_all_groups_blocked():
    n = 1
    reservedSeats = [[1, 2], [1, 4], [1, 6], [1, 8]]

    assert Solution().maxNumberOfFamilies(n, reservedSeats) == 0


def test_reservations_outside_family_seats():
    n = 2
    reservedSeats = [[1, 1], [1, 10], [2, 1], [2, 10]]

    assert Solution().maxNumberOfFamilies(n, reservedSeats) == 4


def test_left_group_only():
    n = 1
    reservedSeats = [[1, 6], [1, 8]]

    assert Solution().maxNumberOfFamilies(n, reservedSeats) == 1


def test_right_group_only():
    n = 1
    reservedSeats = [[1, 2], [1, 4]]

    assert Solution().maxNumberOfFamilies(n, reservedSeats) == 1