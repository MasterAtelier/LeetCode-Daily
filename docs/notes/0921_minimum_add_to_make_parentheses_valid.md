# Minimum Add to Make Parentheses Valid

## Problem

- **Name:** Minimum Add to Make Parentheses Valid (LeetCode 921)
- **Difficulty:** Medium
- **Category:** Greedy / Strings / Prefix Balance

Given a string containing only `(` and `)`, return the minimum number of parentheses that must be inserted to make the whole string valid.

## Core Pattern

- **Main algorithmic pattern:** Greedy unmatched-parenthesis counting.
- **Recognition cues:** A one-pass delimiter sequence asks for the minimum insertions needed to repair unmatched opens and closes.
- **Why it applies:** A closing parenthesis with no earlier unmatched opening cannot be repaired by any later character, so it forces one inserted opening immediately. Any unmatched openings left after the scan each force one inserted closing.

## Intuition

Treat the scan as matching each `)` to the nearest available unmatched `(`. Keep a count of unmatched openings. When a close arrives and that count is positive, it consumes one opening. When the count is zero, the close is unmatched and requires an inserted opening, so increment the answer. At the end, every still-unmatched opening requires an inserted close.

## Brute Force

- **Idea:** Try candidate insertions of parentheses and check each resulting string until a valid string is found with the fewest additions.
- **Complexity:** The number of insertion choices grows combinatorially with the number of added characters; validating each candidate takes linear time.
- **Why it is inefficient:** The input has local matching structure that can be accounted for in one pass without constructing candidate strings.

## Optimal Solution

### Key observations

1. An unmatched `)` forces an inserted `(` before it; later characters cannot retroactively match it.
2. A `)` matches one prior unmatched `(` whenever one is available.
3. Each unmatched `(` remaining at the end forces one inserted `)`.
4. These required insertions are independent, so their sum is the minimum.

### Data structures used

- `count_open`: currently unmatched opening parentheses.
- `count_close`: unmatched closing parentheses that require inserted openings.

### Algorithm explanation

Scan from left to right. Increment `count_open` for each `(`. For each `)`, decrement `count_open` if it is positive; otherwise increment `count_close`. Return the sum of the two counts. The input constraints guarantee that every character is a parenthesis.

## Algorithm

1. Initialize unmatched-open and unmatched-close counts to zero.
2. For each `(`, increase the unmatched-open count.
3. For each `)`, consume an unmatched open if one exists; otherwise record one unmatched close.
4. Return unmatched opens plus unmatched closes.

## Complexity

- **Time:** `O(n)`, since the string is scanned once.
- **Space:** `O(1)`, using two integer counters.

## Edge Cases

- A single `(` needs one inserted `)`.
- A single `)` needs one inserted `(`.
- An already-valid string needs no insertions.
- A prefix with excess closes contributes one insertion for each unmatched close.
- Any unmatched opens remaining at the end contribute one insertion each.
- The maximum input length is 1,000.

## Alternative Approaches

- **Stack:** Push unmatched openings; each closing either pops one or contributes an insertion. The stack stores more information than needed, so its worst-case space is `O(n)` rather than `O(1)`.
- **Final balance with prefix correction:** Track a balance and add one insertion whenever it would become negative, resetting it to zero; add the final balance afterward. This is equivalent to tracking unmatched closes and opens separately.

## Similar Problems

1. **20. Valid Parentheses:** Checks whether the whole string is valid, usually with a stack.
2. **22. Generate Parentheses:** Constructs strings whose every prefix has nonnegative balance.
3. **32. Longest Valid Parentheses:** Uses unmatched delimiters to find valid substring boundaries.
4. **678. Valid Parenthesis String:** Tracks feasible balances when `*` can take several meanings.
5. **1111. Maximum Nesting Depth of Two Valid Parentheses Strings:** Uses running nesting depth to partition a valid sequence.
6. **1249. Minimum Remove to Make Valid Parentheses:** Removes unmatched parentheses instead of inserting missing ones.

## Python Tips

- Integer counters are enough when the task asks only for the number of unmatched delimiters.
- A stack is useful when matching positions must be returned, but avoid storing positions when only a count is needed.

## Interview Discussion

- Prove why an unmatched close must be repaired at its position: no future opening can appear before it.
- Explain why every leftover opening needs exactly one closing insertion.
- Contrast this task with removing invalid parentheses, where the operation and requested output differ.
- If the input has several bracket types, explain why a single balance count is no longer sufficient and a stack is needed.

## Personal Takeaways

- Repair prefix deficits when they occur; later symbols cannot fix an invalid earlier prefix.
- Track only the state the output needs: counts suffice when insertion locations are irrelevant.
- A minimum edit count can sometimes be derived from independent unmatched obligations.
