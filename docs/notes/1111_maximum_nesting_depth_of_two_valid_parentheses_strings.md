# Maximum Nesting Depth of Two Valid Parentheses Strings

## Problem

- **Name:** Maximum Nesting Depth of Two Valid Parentheses Strings
- **Difficulty:** Medium
- **Category:** Greedy / Parentheses / Depth Parity

## Core Pattern

### Main algorithmic pattern
Assign each parenthesis according to the parity of its nesting depth.

### Recognition cues
- A valid nested structure must be split into two valid subsequences.
- The objective minimizes the largest nesting depth among the groups.
- Each opening or closing parenthesis can be assigned consistently using its current depth.

### Why the pattern applies
Alternating ownership by nesting level makes each group's nesting depth about half the original maximum. Keeping the same owner for an opening parenthesis and its matching close preserves balanced subsequences.

## Intuition

Imagine alternating which group owns each layer of nested parentheses. The outermost pair goes to one group, the next nested pair to the other, the next to the first, and so on. The maximum stack height in either group is then minimized: no group receives consecutive nesting levels.

The implementation can track the current depth in one pass. Give the same parity label to both sides of each pair, using the depth of the layer that pair occupies.

## Brute Force

One could enumerate all `2^n` assignments and retain only those that produce two valid subsequences, then choose the assignment minimizing the larger depth. This is infeasible even for modest strings and ignores the structure of matching parentheses. A direct parity assignment solves the problem in linear time.

## Optimal Solution

### Key observations

1. A parenthesis pair must have both characters assigned to the same subsequence for that subsequence to remain balanced.
2. Pairs at equal nesting depth can share an assignment.
3. Assigning alternate nesting levels to alternate groups balances the resulting maximum depths.
4. A running depth identifies the layer of each character: increment before labeling an opening parenthesis and decrement after labeling a closing parenthesis.

### Data structures used

- An integer depth counter.
- An output list with one label per input character.

### Algorithm explanation

Scan the valid parentheses string once. For an opening parenthesis, increase the current depth and label it with the depth parity. For a closing parenthesis, label it with the current depth parity, then decrease the depth. The resulting labels are `0` or `1` and represent the two subsequences.

The submitted implementation starts its counter at `1`; therefore its parity is the inverse of the usual one-based depth parity. This only swaps group labels and produces an equally valid optimal split.

## Algorithm

1. Initialize an empty answer and a depth counter to `1`.
2. For each opening parenthesis, increment depth and append `depth % 2`.
3. For each closing parenthesis, append `depth % 2`, then decrement depth.
4. Return the labels.

## Complexity

- **Time:** `O(n)`, where `n` is the string length.
- **Space:** `O(n)` for the required answer; the scan uses `O(1)` additional space.

## Edge Cases

- A single pair `()` is assigned entirely to one group.
- Fully nested input alternates assignments at every level.
- Sequential pairs all occupy the same depth and may all go to one group.
- The input is guaranteed to be a valid parentheses string, so the scan ends at depth zero.
- The maximum input length is 10,000; the one-pass approach is within the limit.

## Alternative Approaches

- Using zero-based character positions also works: alternating assignment by index parity corresponds to the same depth alternation for a valid parentheses sequence.
- A stack could track matching opens, but it stores information the running depth already provides.
- Exhaustive assignment is unnecessary and exponential.

## Similar Problems

1. **LeetCode 1021 — Remove Outermost Parentheses:** Track nesting depth to identify structural layers.
2. **LeetCode 856 — Score of Parentheses:** Compute values from nesting depth and matching structure.
3. **LeetCode 1614 — Maximum Nesting Depth of the Parentheses:** Track depth in one pass.
4. **LeetCode 921 — Minimum Add to Make Parentheses Valid:** Track unmatched opens and closes.
5. **LeetCode 1249 — Minimum Remove to Make Valid Parentheses:** Use balance tracking or a stack to preserve valid structure.

## Python Tips

- `% 2` gives a compact alternating label for integer depths.
- Update order matters: opens enter a new depth before labeling; closes leave their current depth after labeling.
- `append` keeps output construction linear.

## Interview Discussion

- Explain why matching open and close characters receive the same group label.
- Show that alternating nested levels caps each group's maximum depth at roughly half the original maximum.
- Discuss why either initial parity convention is valid: swapping labels `0` and `1` does not change the split quality.
- If the input might be malformed, add validation by checking that depth never becomes negative and finishes at zero; the stated problem already guarantees validity.

## Personal Takeaways

- For balanced nested strings, depth often captures all the state needed.
- Update state before labeling opens and after labeling closes.
- Alternate ownership by nesting level to divide depth evenly.
- Output labels can be swapped without changing a valid partition's quality.
