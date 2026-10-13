# 3727. Maximum Alternating Sum of Squares

## Problem

- **Difficulty:** Medium
- **Category:** Greedy, Sorting
- Rearrange the integers to maximize the sum of squared values at even positions minus squared values at odd positions.

## Core Pattern

Sort by contribution magnitude, then assign the largest values to positive slots and smallest values to negative slots. The sign of each input is irrelevant because every value is squared.

## Intuition

Each squared value gets coefficient `+1` or `-1`. To maximize the total, pair the largest squares with `+1` and the smallest with `-1`. There are `ceil(n / 2)` positive slots and `floor(n / 2)` negative slots. Alternating between the largest and smallest remaining magnitudes fills those groups.

## Brute Force

Try every permutation and score it. This is O(n! · n) time and is infeasible; rearranging equal square magnitudes also produces redundant cases.

## Optimal Solution

Sort by absolute value. Repeatedly add the largest remaining square, then subtract the smallest remaining square. If one element remains, it occupies a positive slot. Sorting dominates the runtime.

## Algorithm

1. Sort values by absolute value in ascending order.
2. Keep left and right pointers at the smallest and largest magnitudes.
3. Add the square at the right pointer and move it inward.
4. If values remain, subtract the square at the left pointer and move it inward.
5. Return the accumulated score.

## Complexity

- **Time:** O(n log n) for sorting, then O(n) pointer traversal.
- **Space:** O(n) auxiliary space for Python's in-place sort implementation. The list is sorted in place.

## Edge Cases

- One value: it is positive in the score.
- Negative values: sign does not matter after squaring.
- Zeros and repeated absolute values: ties are interchangeable.
- Odd length: one more value is assigned a positive slot.

## Alternative Approaches

Sort the squares directly, subtract the smallest `n // 2` squares, and add the rest. This expresses the same assignment directly. A frequency/counting approach is possible because the value range is bounded, but sorting is simpler and already optimal asymptotically.

## Similar Problems

1. **1403. Minimum Subsequence in Non-Increasing Order** — sort values and greedily select largest contributions.
2. **561. Array Partition** — sorting determines optimal pair assignments.
3. **1046. Last Stone Weight** — repeatedly operate on largest magnitudes using a heap.
4. **870. Advantage Shuffle** — sort and assign values according to contribution/priority.
5. **238. Product of Array Except Self** — signed contributions differ, but careful per-position contribution accounting is central.

## Python Tips

- `nums.sort(key=abs)` sorts in place by magnitude and mutates the input list.
- `x ** 2` clearly expresses squaring; `x * x` is equivalent.
- Python integers grow as needed, so the maximum total is safe from fixed-width overflow.

## Interview Discussion

- Why is sorting by absolute value valid? Because the objective contains only squares.
- Why do the largest magnitudes go in positive slots? Swapping a larger square into a positive slot and a smaller square into a negative slot cannot decrease the score.
- Can the implementation avoid sorting? Possibly with value counting under the stated bounded range, but asymptotic complexity remains linear after counting.
- What is the input side effect? `sort` mutates `nums`; use `sorted(nums, key=abs)` if preserving the input is required.

## Personal Takeaways

- Rewrite rearrangement objectives as assigning coefficients to values.
- Pair the largest values with the most favorable coefficients.
- Identify whether transformations such as squaring erase input properties like sign.
- Check whether an in-place sort's mutation is acceptable.
