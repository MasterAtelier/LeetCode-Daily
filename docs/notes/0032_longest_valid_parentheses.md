# Longest Valid Parentheses

## Problem

- **Name:** Longest Valid Parentheses (LeetCode 32)
- **Difficulty:** Hard
- **Category:** String, Stack, Dynamic Programming

Given a string containing only `(` and `)`, return the length of its longest contiguous well-formed parentheses substring.

## Core Pattern

- **Main pattern:** Stack of indices with invalid-boundary tracking.
- **Recognition cues:** Longest valid contiguous substring; matching delimiters; invalid symbols split the input into independent regions.
- **Why it applies:** The stack tracks unmatched opening positions. An unmatched closing parenthesis marks a boundary that no valid substring can cross. Those two boundary types give the start of every valid range ending at the current index.

## Intuition

For a valid substring ending at index `i`, its beginning is just after the most recent unmatched closing parenthesis, or just after the most recent unmatched opening parenthesis if one remains. Store opening indices on a stack and remember the last unmatched closing index. After processing each closing parenthesis, the top of the stack (or that closing boundary) identifies the preceding invalid position. Subtracting it from `i` gives the valid suffix length.

## Brute Force

- **Idea:** Enumerate every substring and check whether its running balance remains nonnegative and ends at zero.
- **Complexity:** There are O(n²) substrings; checking each takes O(n), for O(n³) time and O(1) extra space. Incremental balance checks reduce the time to O(n²).
- **Why it is inefficient:** It repeats work across overlapping substrings and is unnecessary for a limit of 30,000 characters.

## Optimal Solution

- **Key observations:** Valid parentheses substrings cannot contain an unmatched closing parenthesis or cross an unmatched opening parenthesis.
- **Data structures:** A stack of opening-parenthesis indices, an integer for the most recent unmatched closing index, and an integer maximum.
- **Algorithm:** Push indices for `(`. For `)`, if there is no opening to match, record this index as the new invalid boundary. Otherwise pop one opening. The current valid suffix starts after the unmatched opening at the stack top when the stack remains nonempty; when it becomes empty, it starts after the last unmatched closing boundary. Update the maximum length.

## Algorithm

1. Initialize an empty stack, `last_invalid_index = -1`, and `max_length = 0`.
2. Scan the string from left to right.
3. Push the current index for each `(`.
4. For each `)`, if the stack is empty, mark this index as the latest invalid boundary.
5. Otherwise pop a matching opening index. If the stack is now empty, measure from `last_invalid_index`; otherwise measure from the opening index still at the top.
6. Return the largest measured length.

## Complexity

- **Time:** O(n), because every character is processed once and each index is pushed and popped at most once.
- **Space:** O(n) in the worst case, when the input contains only opening parentheses.

## Edge Cases

- Empty input returns 0.
- An unmatched closing parenthesis resets the valid region.
- Unmatched opening parentheses remain as boundaries for later valid suffixes.
- A fully nested or fully concatenated valid string may use the entire input.
- The maximum input length is 30,000.

## Alternative Approaches

- **Dynamic programming:** `dp[i]` stores the longest valid substring ending at `i`; O(n) time and space, with more involved transitions.
- **Two directional scans:** Balance counters find runs where counts match; scanning both directions is needed to handle excess openings and closings. This uses O(1) auxiliary space.
- **Stack with a sentinel:** A sentinel index can combine the invalid-boundary logic into one stack. The submitted implementation tracks the closing boundary separately, which is equally linear and clear.

## Similar Problems

- **20. Valid Parentheses:** Checks whether the entire delimiter string is valid, rather than finding a longest valid substring.
- **22. Generate Parentheses:** Builds valid strings by maintaining prefix-balance constraints.
- **921. Minimum Add to Make Parentheses Valid:** Counts unmatched opening and closing parentheses.
- **1249. Minimum Remove to Make Valid Parentheses:** Removes unmatched delimiters while preserving order.
- **678. Valid Parenthesis String:** Adds wildcard choices to the balance constraints.
- **1111. Maximum Nesting Depth of Two Valid Parentheses Strings:** Uses parentheses depth to divide a valid sequence.

## Python Tips

- A list is an efficient stack with `append()` and `pop()` at the end.
- `enumerate(s)` yields each character and index together.
- Store positions rather than characters when substring lengths depend on boundaries.

## Interview Discussion

- Explain why each invalid delimiter separates regions that cannot form a valid substring across it.
- Compare the stack approach with the O(1)-space two-pass balance method.
- Discuss how the method changes if the alphabet includes multiple delimiter types or non-parenthesis characters.
- Clarify that the requested substring must be contiguous; a subsequence version is a different problem.

## Personal Takeaways

- For substring length problems, indices often carry more useful information than values.
- Unmatched delimiters act as hard boundaries.
- Every closing delimiter either creates a boundary or completes a valid suffix.
- A one-pass stack solution can be optimal even when the task asks for a maximum over all substrings.
