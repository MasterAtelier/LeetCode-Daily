# Score of Parentheses

## Problem

- **Name:** Score of Parentheses (LeetCode 856)
- **Difficulty:** Medium
- **Category:** Strings / Parentheses / Depth Tracking

Given a balanced parentheses string, calculate its score using `()` = 1, concatenation as addition, and wrapping a string in parentheses as doubling its score.

## Core Pattern

- **Main algorithmic pattern:** One-pass nesting-depth tracking with weighted primitive contributions.
- **Recognition cues:** The input is balanced and nested; each smallest `()` contributes a value that depends on how deeply it is nested.
- **Why it applies:** A primitive `()` at depth `d` contributes `2**d`. The scan can identify each primitive from adjacent characters and maintain its depth with one counter.

## Intuition

Expand the score rules mentally: wrapping doubles a group's score, so every enclosing pair doubles each primitive `()` inside it. Therefore, each primitive contributes one multiplied by two once per enclosing pair. Scan adjacent characters; whenever they form `()`, add the power of two for its current nesting depth. Update the depth as each opening or closing parenthesis is passed.

## Brute Force

- **Idea:** Recursively parse the string into primitive and wrapped groups, compute each group's score, then sum concatenated groups.
- **Complexity:** `O(n)` time to parse the string, with up to `O(n)` recursion/parse state.
- **Why it is inefficient:** It is not asymptotically slower, but it introduces recursive parsing state when a depth counter is enough.

## Optimal Solution

### Key observations

1. Every balanced string decomposes into concatenated components, so their scores add.
2. Every primitive `()` contributes `1` before wrapping.
3. Each enclosing pair doubles that primitive's contribution; at depth `d`, its contribution is `2**d`.
4. A `()` is detected by checking adjacent characters, while the running depth gives its enclosing depth.

### Data structures used

- An integer accumulator for the total score.
- An integer depth counter; no stack is required because the input is guaranteed balanced.

### Algorithm explanation

Iterate through adjacent character pairs. If a pair is `()`, add `1 << depth` to the total. After considering the pair, update the depth based on its first character: increment for `(` and decrement for `)`. The final total is the score.

## Algorithm

1. Initialize `score` and `depth` to zero.
2. For each adjacent pair `(a, b)`, if it is `()`, add `2**depth` to `score`.
3. Update `depth` according to `a`.
4. Return `score`.

## Complexity

- **Time:** `O(n)`, one pass over the adjacent pairs.
- **Extra space:** `O(1)` auxiliary counters. The integer values themselves can grow with the answer's bit length.

## Edge Cases

- Minimum input `()` has score 1.
- A deeply nested primitive gets a large power-of-two contribution.
- Adjacent top-level groups add their scores, as in `()()`.
- Mixed nested and concatenated structures combine doubling and addition, as in `(()())`.
- The input is guaranteed balanced, so validation of malformed strings is outside the task.

## Alternative Approaches

- **Stack of partial scores:** Push a score for each opening parenthesis and combine it when a matching close is reached. This directly mirrors the recursive definition but uses `O(n)` stack space.
- **Recursive parsing:** Compute a wrapped group's score as twice its interior score and add sibling groups. This can use `O(n)` call stack in the deepest nesting case.
- **Depth-weighted primitive scan:** The submitted approach avoids storing group state and uses constant auxiliary space.

## Similar Problems

1. **20. Valid Parentheses:** Uses a stack to validate matching bracket types; this problem assumes validity and computes a score.
2. **22. Generate Parentheses:** Builds valid strings while tracking prefix depth.
3. **32. Longest Valid Parentheses:** Uses delimiter structure to find valid substring boundaries.
4. **678. Valid Parenthesis String:** Tracks possible depths when wildcard characters create multiple choices.
5. **921. Minimum Add to Make Parentheses Valid:** Tracks prefix balance and unmatched delimiters.
6. **1111. Maximum Nesting Depth of Two Valid Parentheses Strings:** Uses current depth to make assignment decisions.

## Python Tips

- `itertools.pairwise(s)` yields adjacent character pairs without slicing the whole string.
- `1 << depth` computes `2**depth` using a bit shift.
- `pairwise` requires Python 3.10 or later.

## Interview Discussion

- Prove why a primitive at depth `d` contributes `2**d`: each enclosing pair applies the wrapping rule once.
- Explain why the depth at the `(` of a primitive is exactly the number of enclosing pairs.
- Contrast this constant-state scan with a stack solution, which more directly mirrors the grammar but stores more state.
- Clarify that the method relies on the problem's guarantee that the input is balanced.

## Personal Takeaways

- Translate recursive scoring rules into a contribution per primitive unit.
- Track only the depth needed to weight each contribution.
- Use a stack when matching structure must be validated or retained; use a counter when validity is guaranteed and only depth matters.
