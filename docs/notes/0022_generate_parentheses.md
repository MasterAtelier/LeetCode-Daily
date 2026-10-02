# Generate Parentheses

## Problem

- **Name:** Generate Parentheses
- **Difficulty:** Medium
- **Category:** Backtracking / Combinatorics / Strings

## Core Pattern

### Main algorithmic pattern
Backtracking with feasibility pruning: build a valid prefix and only branch when the next parenthesis cannot make the prefix invalid.

### Recognition cues
- Generate every string satisfying structural constraints.
- A partial answer can be rejected as soon as a prefix violates a rule.
- The output size is combinatorial, so constructing each valid output is unavoidable.

### Why the pattern applies
A parenthesis string is valid precisely when every prefix has at least as many opening as closing parentheses and the final counts are equal. The recursion tracks those counts and admits only choices that preserve the prefix condition.

## Intuition

At every position, an opening parenthesis is allowed while fewer than `n` have been used. A closing parenthesis is allowed only when it can match an opening parenthesis already placed. This means every path in the recursion tree is already a valid prefix; there is no need to generate arbitrary strings and validate them afterward.

## Brute Force

Generate all `2^(2n)` strings of length `2n` and check which are balanced. This spends time on strings with the wrong counts and on prefixes that are invalid early. Its time is `O(2^(2n) * n)` when each candidate is checked in linear time.

## Optimal Solution

### Key observations

1. Exactly `n` opening and `n` closing parentheses must be used.
2. A prefix with more closes than opens can never be repaired.
3. Once both counts reach `n`, the sequence is complete and valid by construction.
4. There are `C_n` valid outputs, where `C_n` is the nth Catalan number; producing them requires at least `Ω(n * C_n)` time and output space.

### Data structures used

- A list containing completed strings.
- Recursion state: the current prefix and counts of opens and closes used.

### Algorithm explanation

The recursive helper first emits a result when the current prefix has length `2n`. Otherwise it branches by adding `(` if the opening quota is not reached, and by adding `)` if closes remain fewer than opens. The constraints guarantee that all emitted strings are balanced and unique.

## Algorithm

1. Start with an empty prefix and zero opens and closes.
2. If the prefix length is `2n`, append it to the answer.
3. If fewer than `n` opens have been used, recurse with an opening parenthesis.
4. If closes are fewer than opens, recurse with a closing parenthesis.
5. Return the accumulated strings.

## Complexity

- **Time:** `Θ(n * C_n)` to construct all `C_n` strings of length `2n` (the recursion has `O(C_n)` prefix states, each string extension copies up to `O(n)` characters).
- **Space:** `Θ(n * C_n)` for returned strings. The recursion depth is `O(n)`; because each frame retains its own immutable prefix string, the active recursion path can hold `O(n^2)` characters in total.

## Edge Cases

- `n = 1` produces `()`.
- `n = 0` produces `['']` under this implementation; LeetCode's constraints use `n >= 1`.
- The largest allowed `n` produces many outputs, but the required output itself is Catalan-sized.
- The closing branch must be gated by `close < open` to prevent invalid prefixes.

## Alternative Approaches

- Generate all strings and validate afterward: correct but explores many impossible prefixes.
- Use a mutable character list with append/pop to avoid repeatedly copying prefixes; asymptotic output-sensitive complexity remains `Θ(n * C_n)`.
- Dynamic programming can combine results for smaller sizes, but is less direct than constrained backtracking for generating every string.

## Similar Problems

1. **LeetCode 22 — Generate Parentheses:** This problem; constrained backtracking over balanced prefixes.
2. **LeetCode 301 — Remove Invalid Parentheses:** Search over edits while minimizing removals.
3. **LeetCode 241 — Different Ways to Add Parentheses:** Recursively enumerate results by splitting an expression.
4. **LeetCode 46 — Permutations:** Backtracking over choices with a used-element constraint.
5. **LeetCode 78 — Subsets:** Enumerate all include/exclude paths without a prefix-validity constraint.

## Python Tips

- Use meaningful state names such as `open_count` and `close_count`; avoid shadowing the built-in `open`.
- The submitted helper parameter `max_pairs` is clear and avoids shadowing `max`.
- For this constraint size, immutable string concatenation is acceptable; a list path with append/pop can reduce intermediate copying.

## Interview Discussion

- Explain why `close_count < open_count` is exactly the condition that preserves prefix validity.
- Explain why every complete path has exactly `n` pairs and is therefore balanced.
- Ask about output-sensitive complexity: the answer itself contains `C_n` strings, so an algorithm cannot run in polynomial time in `n` while explicitly returning them all.
- Clarify whether `n = 0` is in scope if discussing behavior outside LeetCode constraints.

## Personal Takeaways

- Track the smallest state that determines whether a partial candidate can still succeed.
- Prune invalid prefixes at the moment they arise.
- When every valid result is required, measure complexity against the output size.
