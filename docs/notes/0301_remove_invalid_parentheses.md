# Remove Invalid Parentheses

## Problem

- **Name:** Remove Invalid Parentheses (LeetCode 301)
- **Difficulty:** Hard
- **Category:** String, Breadth-First Search, Parentheses Validation

Given a string of lowercase letters and parentheses, remove the fewest parentheses needed to make it valid. Return every distinct valid result that uses that minimum number of removals.

## Core Pattern

- **Main pattern:** Breadth-first search over edit states.
- **Recognition cues:** Make the fewest one-step edits; several minimum answers may exist; each state can generate neighboring states by deleting one allowed character.
- **Why it applies:** Each deletion has equal cost. BFS checks all strings after zero deletions, then one deletion, then two, and so on. The first layer containing valid strings is therefore the minimum-removal layer.

## Intuition

Treat each candidate string as a state. From a state, create neighbors by removing one parenthesis. Since every removal costs one, BFS naturally groups candidates by how many removals produced them. A set merges identical strings reached by removing repeated parentheses in different positions. Once a layer contains valid strings, no later layer can be a minimum answer, so return every valid string from that layer.

## Brute Force

- **Idea:** Try every subset of the parentheses to remove, then check whether the remaining string is valid. Keep the valid results with the fewest removals.
- **Complexity:** With `p` parentheses and string length `n`, there can be `2^p` subsets, each taking up to `O(n)` to construct and validate: `O(n * 2^p)` time, plus candidate storage.
- **Why it is inefficient:** It explores candidates with many removals even when a valid result exists after only a few. BFS stops as soon as it reaches the first valid layer.

## Optimal Solution

- **Key observations:**
  - Parentheses validity requires every prefix to have at least as many opening as closing parentheses.
  - The final opening and closing counts must be equal.
  - Removing a parenthesis costs one, so the number removed is exactly the BFS depth.
  - Different removal sequences can produce the same string, so states should be deduplicated.
- **Data structures:** A set for the current BFS layer, a set for the next layer, and a running balance in the validity check.
- **Algorithm explanation:** Check all strings at the current depth. If any are valid, return all of them. Otherwise remove each parenthesis in turn to build the next layer, skipping letters. Continue until a valid layer is found.

## Algorithm

1. Define a validator that scans a candidate with a balance counter.
2. Increase the balance for `(` and decrease it for `)`; letters leave it unchanged.
3. Reject immediately if the balance becomes negative. At the end, accept only if the balance is zero.
4. Initialize the current BFS layer with the original string.
5. If the current layer contains valid strings, return all of them.
6. Otherwise, for every string in the layer, remove each parenthesis once and add the resulting strings to a set for the next layer.
7. Replace the current layer with the next layer and repeat.

## Complexity

Let `n` be the total string length and `p` the number of parentheses. There are at most `2^p` distinct deletion states. Each state scans up to `n` characters for validation and can generate up to `p` children, each requiring `O(n)` string copying.

- **Time:** `O(n * (p + 1) * 2^p)` worst case, including the case with no parentheses.
- **Space:** `O(n * 2^p)` as a conservative upper bound for stored candidate strings. The problem limits `p` to 20 and `n` to 25.

## Edge Cases

- The input is already valid, so the original string is the only answer.
- All parentheses are invalid, so the answer may contain no parentheses or be the empty string.
- Letters must remain in their original order and cannot be deleted.
- Repeated parentheses can lead to the same candidate through multiple deletion paths; sets prevent duplicate answers.
- Several different strings can be valid at the same minimum removal count.

## Alternative Approaches

- **DFS/backtracking with removal counts:** First count the minimum number of unmatched opening and closing parentheses, then recurse while removing exactly those counts. It can avoid visiting invalid shallower BFS layers, but needs careful duplicate-skipping and pruning.
- **Generate all subsequences:** Correct when paired with a minimum-removal comparison, but it may do unnecessary work after discovering better candidates.
- **Two-pass directional removal:** Efficiently produces one valid repaired string, but additional branching is needed to return every distinct minimum result.

## Similar Problems

- **20. Valid Parentheses:** Checks one complete delimiter string using balance or a stack.
- **22. Generate Parentheses:** Builds valid strings while pruning prefixes with too many closing parentheses.
- **32. Longest Valid Parentheses:** Uses unmatched delimiters as boundaries to find a longest valid substring.
- **678. Valid Parenthesis String:** Tracks feasible balances when a wildcard has multiple meanings.
- **921. Minimum Add to Make Parentheses Valid:** Counts unmatched delimiters when insertion is allowed.
- **1249. Minimum Remove to Make Valid Parentheses:** Returns one valid string after the minimum removals.
- **127. Word Ladder:** BFS levels represent the number of transformations in a shortest path.
- **752. Open the Lock:** BFS finds the fewest equal-cost moves between states.

## Python Tips

- A `set` is useful both for deduplicating a BFS layer and for returning unique candidates.
- Strings are immutable; slicing plus concatenation creates a new string, which costs `O(n)`.
- The problem allows any answer order, so set iteration order does not affect correctness.
- `filter(is_valid, level)` is concise; a list comprehension can make the filtering condition more explicit.

## Interview Discussion

- Explain why BFS depth equals the number of removed parentheses and why stopping after the first valid layer proves minimality.
- Explain the validity invariant: no prefix may have negative balance, and the final balance must be zero.
- Discuss why the set is necessary when repeated parentheses can produce the same string by deleting different indices.
- State the exponential worst case in terms of the number of parentheses, and relate it to the maximum of 20 parentheses.
- Ask whether output order matters. Here it does not; if it did, results would need explicit ordering.

## Personal Takeaways

- Equal-cost edits are a strong signal for BFS when the goal is the fewest edits.
- Validate constraints with an invariant that catches invalid prefixes early.
- Deduplicate states whenever multiple paths can reach the same result.
- Stop at the first successful BFS depth, but finish scanning that entire layer to collect every tied answer.
