# 2897. Apply Operations on Array to Maximize Sum of Squares

## Problem

- **Name:** Apply Operations on Array to Maximize Sum of Squares
- **Difficulty:** Hard
- **Category:** Bit Manipulation, Greedy, Counting

Given `nums` and `k`, repeatedly choose two values and replace them with their bitwise AND and OR. Choose `k` values from the resulting array to maximize the sum of their squares, modulo `10^9 + 7`.

## Core Pattern

### Main Pattern: Greedy Bit Redistribution

Count the available copies of every bit, then distribute those bits to form the largest possible `k` values.

### Recognition Cues

- The operation transforms two values with AND and OR.
- A per-bit quantity may be conserved even though individual values change.
- The objective is a sum of squares, which rewards concentrating value into fewer large terms.

### Why It Applies

For each bit, `(a & b) + (a | b) = a + b`, so the number of copies of that bit across the array is invariant. Conversely, the operation can move a bit from one value to another while preserving its total count. To maximize squares, pack the available bits together into each selected value before moving to the next one. This makes the selected values as large and concentrated as possible.

## Intuition

The actual numbers can change, but the inventory of each bit cannot. Imagine one pile for each bit position. Building one output at a time, take one copy of every bit whose pile is nonempty. This creates the largest available value; repeating it creates the most concentrated distribution. The square function is convex, so concentrating the same total bit value into fewer numbers increases the sum of squares.

## Brute Force

Try every sequence of pair operations and every choice of `k` final elements. This is infeasible: there are many operation sequences, and the array can contain up to `10^5` values. The state space is unnecessary because only bit counts matter.

## Optimal Solution

### Key Observations

1. For every bit position, AND plus OR has the same bit sum as the original pair. Thus its count across the array is conserved.
2. Each bit can be assigned independently when constructing output numbers.
3. To maximize the sum of squares, form each selected number with one available copy of every bit, then continue until `k` numbers are formed.

### Data Structures

An array of 30 integer counters is sufficient because `nums[i] <= 10^9 < 2^30`.

### Algorithm

1. Count set bits at positions 0 through 29 across all values.
2. Repeat `k` times:
   - Start with a zero value.
   - For each bit position with a positive count, set that bit in the value and decrement its count.
   - Add the square of the constructed value to the answer modulo `10^9 + 7`.
3. Return the answer.

## Complexity

- **Time:** O(30n + 30k), effectively O(n + k) for fixed-width integers.
- **Auxiliary space:** O(30), effectively O(1).

## Edge Cases

- `k = 1`: all available bits are assembled into one value.
- `k = len(nums)`: all bit copies are placed into values, and no bit is lost.
- Repeated values: counts naturally accumulate.
- Large values: squares can exceed 64-bit limits in some languages, so apply modulo during accumulation; Python integers do not overflow.
- A bit count can exceed `k`: it appears in the first several constructed values.

## Alternative Approaches

- A priority queue can repeatedly choose which numbers receive bits, but the fixed per-bit construction is simpler and requires constant space.
- Simulating legal AND/OR operations is possible but wastes work and obscures the conserved bit counts.
- Sorting the original values alone cannot account for bits that operations can transfer between values.

## Similar Problems

- **1863. Sum of All Subset XOR Totals:** Uses bitwise contribution reasoning, though it counts subsets rather than redistributing bits.
- **191. Number of 1 Bits:** Inspects individual bit positions.
- **268. Missing Number:** Uses XOR conservation rather than bit-count conservation.
- **2333. Minimum Sum of Squared Difference:** Also optimizes a sum of squares, but decreases differences rather than concentrating bit values.
- **2231. Largest Number After Digit Swaps by Parity:** Greedily redistributes positions within independent groups.

## Python Tips

- `(value >> bit) & 1` extracts a bit as 0 or 1.
- `value |= 1 << bit` sets a bit.
- In Python, `value * value` is safe for arbitrarily large integers; modular reduction is still required by the problem.

## Interview Discussion

- Prove conservation per bit using `(a & b) + (a | b) = a + b`.
- Explain why packing maximizes a convex objective such as the sum of squares.
- Discuss whether the greedy construction remains valid for a different objective, such as maximizing the sum (where the total is invariant).
- Generalize the loop bound if the input value bound changes.

## Personal Takeaways

- Inspect bitwise operations for per-bit invariants before simulating them.
- Convex objectives often reward concentration; concave objectives often reward balance.
- Build only the values the answer uses, and consume a count as each bit is assigned.
