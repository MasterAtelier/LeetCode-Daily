# 2778. Sum of Squares of Special Elements

## Problem

- **Name:** Sum of Squares of Special Elements
- **Difficulty:** Easy
- **Category:** Arrays, Index Arithmetic

Given an integer array `nums`, an element is special when its **1-indexed** position divides the array length. Return the sum of the squares of the special elements.

## Core Pattern

### Main Pattern: Single-Pass Filtering by an Index Property

Scan each element once and use its position to decide whether it contributes to the answer.

### Recognition Cues

- An array element is selected based on its position.
- The condition relates the index to the array length or another fixed value.
- Only an aggregate of selected values is needed.

### Why It Applies

Every candidate can be classified independently in constant time. There is no need to collect special elements first or enumerate the divisors separately.

## Intuition

The statement uses 1-based positions while Python uses 0-based indexes. For Python index `i`, the corresponding position is `i + 1`. That position is special exactly when `n % (i + 1) == 0`, where `n` is the array length. Add the square of the value whenever this condition holds.

## Brute Force

One possible approach is to enumerate all divisors of `n`, then look up and square the values at those positions. This can work, but it adds divisor-enumeration logic and still requires identifying the matching positions. A direct scan is simpler and already optimal because each array element may need inspection.

## Optimal Solution

### Key Observations

1. A special element's 1-based position must divide `n`.
2. Convert a Python index `i` to its 1-based position with `i + 1`.
3. Each element can be checked and accumulated during one traversal.

### Data Structures

Only scalar variables are needed: the array length and a running sum.

### Algorithm

1. Set `n` to the array length and initialize the sum to zero.
2. Visit each element at zero-based index `i`.
3. If `n` is divisible by `i + 1`, add the element squared to the sum.
4. Return the sum.

## Complexity

- **Time:** O(n), for one pass through the array.
- **Auxiliary space:** O(1).

## Edge Cases

- **One element:** Position 1 divides 1, so its square is included.
- **No interior divisor positions:** Only positions 1 and `n` qualify.
- **Duplicate values:** Each qualifying position contributes independently.
- **All values equal:** Multiply the number of qualifying positions by the common value squared.

## Alternative Approaches

- Enumerate divisors up to `sqrt(n)` and add the corresponding values. This can reduce checks for very large arrays if values can be accessed directly, but is not asymptotically better than the necessary O(n) input traversal here.
- Build a list of special values and then sum their squares. This uses O(n) additional space without improving time.

## Similar Problems

- **2058. Find the Minimum and Maximum Number of Nodes Between Critical Points:** Detect qualifying positions during a traversal and aggregate their positions.
- **3622. Check Divisibility by Digit Sum and Product:** Apply a divisibility condition to an accumulated value.
- **1. Two Sum:** Scan once and update an aggregate lookup structure as candidates are encountered.
- **1480. Running Sum of 1d Array:** Compute an aggregate while traversing an array once.
- **485. Max Consecutive Ones:** Track a property over a single pass.

## Python Tips

- `enumerate(nums)` gives each value and its zero-based index together.
- Use `index + 1` when the problem describes positions with one-based indexing.
- The modulo operator `%` checks divisibility: `a % b == 0` means `b` divides `a`.
- `value * value` avoids a floating-point result, unlike `value ** 2.0`.

## Interview Discussion

- Clarify whether positions are zero-based or one-based before writing the condition.
- Explain why every item must be considered, giving an O(n) lower bound in the general case.
- If asked to process many arrays sharing the same length, identify the divisor positions once and reuse them where practical.

## Personal Takeaways

- Translate one-based positions explicitly when coding in Python.
- Combine filtering and aggregation when each item can be handled independently.
- A single pass with a scalar accumulator often gives both the simplest and optimal solution.
