# Valid Parenthesis String

## Problem

- **Name:** Valid Parenthesis String (LeetCode 678)
- **Difficulty:** Medium
- **Category:** Greedy / Strings / Stack

Given a string of `(`, `)`, and `*`, determine whether it can be made valid. Each `*` may become `(`, `)`, or an empty string.

## Core Pattern

- **Main algorithmic pattern:** Greedy range of possible balances.
- **Recognition cues:** A wildcard has a small set of local choices, and the question asks whether at least one assignment satisfies a prefix-balance rule.
- **Why the pattern applies:** After each character, all reachable counts of unmatched opening parentheses form a continuous interval. Tracking its minimum and maximum is enough; the actual assignments do not need to be stored.

## Intuition

A fixed parenthesis string is valid when no prefix has more closing than opening parentheses and the final balance is zero. A `*` can lower the balance by one, leave it unchanged, or raise it by one. Instead of branching into three strings for every star, track the smallest and largest balances that remain possible. If even the largest balance becomes negative, a prefix cannot be repaired. At the end, validity is possible exactly when the smallest balance is zero.

## Brute Force

- **Idea:** Try all three interpretations of every `*`, then check whether any resulting string is balanced.
- **Complexity:** `O(3^k * n)` time in the worst case, where `k` is the number of stars and `n` is the string length. A recursive search uses `O(n)` stack space.
- **Why it is inefficient:** Many branches represent similar balances, and the number of assignments grows exponentially.

## Optimal Solution

### Key observations

1. For each processed prefix, possible unmatched-open counts occupy a continuous range `[min_open, max_open]`.
2. An opening parenthesis raises both endpoints.
3. A closing parenthesis lowers both endpoints; the lower endpoint is clamped at zero because negative balances are not allowed for a valid prefix.
4. A star can act as a close, an open, or nothing, so it may lower the minimum or raise the maximum.
5. If `max_open` becomes negative, there are more forced closes than any available opens or stars can cover.
6. At the end, `min_open == 0` means some choice of star interpretations reaches exactly zero.

### Data structures used

- Two integer bounds, `min_open` and `max_open`.

### Algorithm explanation

Scan left to right while maintaining the smallest and largest feasible unmatched-open counts. Update both counts according to the current character, clamping the minimum to zero. If the maximum drops below zero, return false immediately. Once the scan ends, return whether the minimum is zero.

## Algorithm

1. Initialize the minimum and maximum possible unmatched-open counts to zero.
2. For `(`, increment both counts.
3. For `)`, decrement both counts and clamp the minimum to zero.
4. For `*`, decrement and clamp the minimum, and increment the maximum.
5. If the maximum is negative at any point, return false.
6. Return whether the minimum is zero after the full scan.

## Complexity

- **Time:** `O(n)`, with one pass over the string.
- **Space:** `O(1)`, using two counters.

## Edge Cases

- A single `(` or `)` is invalid.
- A single `*` is valid because it may be empty.
- A leading `)` makes the prefix impossible immediately.
- Multiple stars may need different interpretations in the same string.
- A string may be valid even if treating every star the same way would fail, as in `(*))`.

## Alternative Approaches

- **Two stacks of indices:** Track unmatched `(` positions and `*` positions. Match closing parentheses first with real opens, then use later stars as opens. This takes `O(n)` time and `O(n)` space.
- **Dynamic programming:** Track reachable balances after each character. This is direct but can take `O(n^2)` time and space when represented as a table.
- **Backtracking:** Explore each of the three meanings of `*`. This is exponential in the number of stars.

## Similar Problems

1. **20. Valid Parentheses:** Validate a fixed bracket string with a stack.
2. **22. Generate Parentheses:** Construct strings whose prefixes maintain a nonnegative balance.
3. **32. Longest Valid Parentheses:** Use unmatched delimiters to find valid ranges in a fixed string.
4. **921. Minimum Add to Make Parentheses Valid:** Count unmatched opens and closes.
5. **1249. Minimum Remove to Make Valid Parentheses:** Remove unmatched delimiters while preserving order.
6. **2116. Check if a Parentheses String Can Be Valid:** Determine feasibility when certain positions can be changed.

## Python Tips

- `max(0, value)` concisely clamps the minimum reachable balance to zero.
- Use separate names for the bounds; they represent different feasible assignments, not one evolving balance.
- With only three input characters guaranteed, an `else` branch safely represents `*`.

## Interview Discussion

- Explain why reachable balances stay contiguous: each star contributes choices that differ by one, so they fill the integer values between the new endpoints.
- Explain the two failure conditions separately: a negative maximum means a prefix cannot be balanced; a positive minimum at the end means every assignment leaves unmatched opens.
- Compare the constant-space interval approach with the two-stack approach, which gives more detail about which positions are matched.
- Ask how the method changes if a wildcard has a different set of allowed tokens or if there are multiple bracket types.

## Personal Takeaways

- When choices differ only in a small numeric state, track the reachable range instead of enumerating choices.
- Enforce prefix validity as the scan proceeds; a later character cannot fix an already negative prefix balance.
- Clamp only the minimum balance at zero, while a negative maximum signals impossibility.
- Final validity is a reachability question: zero must remain among the possible ending balances.
