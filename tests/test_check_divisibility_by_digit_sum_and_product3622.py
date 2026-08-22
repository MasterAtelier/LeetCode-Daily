from problems.check_divisibility_by_digit_sum_and_product3622 import Solution


def test_example1():
    n = 99

    assert Solution().checkDivisibility(n) is True


def test_example2():
    n = 23

    assert Solution().checkDivisibility(n) is False


def test_single_digit_divisible():
    n = 1

    assert Solution().checkDivisibility(n) is False


def test_single_digit_zero():
    n = 0

    assert Solution().checkDivisibility(n) is True


def test_number_containing_zero():
    n = 10

    assert Solution().checkDivisibility(n) is True


def test_number_containing_zero_not_divisible():
    n = 20

    assert Solution().checkDivisibility(n) is True


def test_multiple_digits():
    n = 123

    assert Solution().checkDivisibility(n) is False


def test_divisible_number():
    n = 36

    assert Solution().checkDivisibility(n) is False


def test_non_divisible_number():
    n = 37

    assert Solution().checkDivisibility(n) is False


def test_repeated_digits():
    n = 111

    assert Solution().checkDivisibility(n) is False