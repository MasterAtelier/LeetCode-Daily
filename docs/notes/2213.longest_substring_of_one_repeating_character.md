# 2213 — Longest Substring of One Repeating Character

## Problem

- **Name:** Longest Substring of One Repeating Character
- **Difficulty:** Hard
- **Category:** Segment Tree

## Core Pattern

### Main Algorithmic Pattern

**Segment Tree with a custom merge state for point updates.**

Each segment stores exactly the information its parent needs to determine the longest contiguous run after two adjacent segments are merged.

### Recognition Cues

Look for problems where:

- The input is a mutable array/string.
- There are many point updates such as "change index `i` to character `c`".
- After every update, a global/range aggregate must be reported.
- The aggregate depends on relationships between adjacent elements.
- Recomputing the whole answer after every update would be too slow.

The important signal here is:

> **Point updates + global longest contiguous property after every update.**

### Why the Pattern Applies

A character update only changes one position, so only the `O(log n)` segment-tree nodes containing that position need to be recomputed.

The parent cannot store only the best run in each child because a run can cross the boundary between the children. Therefore each node also stores its boundary information.

## Intuition

Think of every segment as a compressed summary of its substring.

For a segment, we need to know:

1. Its total length.
2. The length of its longest equal-character prefix.
3. The length of its longest equal-character suffix.
4. The longest equal-character run anywhere inside it.
5. Its first character.
6. Its last character.

When two adjacent segments are merged, there are only three possibilities for the best run:

- It is completely inside the left segment.
- It is completely inside the right segment.
- It crosses the boundary.

A crossing run exists exactly when:

`left.last_char == right.first_char`

In that case its length is:

`left.suffix + right.prefix`

The prefix and suffix can also be extended across the boundary, but only when the entire corresponding child segment consists of that same character.

This is the key segment-tree design insight:

> **Do not ask "what should the tree store?" in the abstract. Ask "what information does a parent need to merge two children correctly?"**

## Brute Force

### Idea

After each character update:

1. Apply the update.
2. Scan the entire string.
3. Track the current equal-character run.
4. Track the maximum run.
5. Append the maximum.

### Complexity

- Each query requires `O(n)`.
- For `q` queries: **O(nq)**.
- Extra space: **O(1)** apart from the mutable string representation.

### Why It Is Inefficient

The same unchanged portions of the string are repeatedly scanned after every update.

With many queries, this becomes too expensive.

## Optimal Solution

### Key Observations

- A point update affects only one leaf.
- Therefore only the ancestors of that leaf can have changed summaries.
- A segment's answer cannot be represented by only its internal best run because a run can cross its midpoint.
- The first and last characters allow us to determine whether two neighboring runs can connect.
- Prefix and suffix lengths tell us how large a boundary-crossing run can become.
- The global answer is always the `best` value stored at the root.

### Data Structures Used

A **segment tree** with one custom node per segment.

Node state:

`[length, prefix, suffix, best, first_char, last_char]`

Where:

- `length` = segment length.
- `prefix` = longest equal-character prefix.
- `suffix` = longest equal-character suffix.
- `best` = longest equal-character substring anywhere in the segment.
- `first_char` = first character of the segment.
- `last_char` = last character of the segment.

### Merge Logic

Given `left` and `right`:

1. `length = left.length + right.length`.
2. Start `best` as `max(left.best, right.best)`.
3. Start `prefix` as `left.prefix`.
4. If the entire left segment is one character and its last character equals the right first character, extend the prefix by `right.prefix`.
5. Start `suffix` as `right.suffix`.
6. If the entire right segment is one character and its first character equals the left last character, extend the suffix by `left.suffix`.
7. If `left.last_char == right.first_char`, consider `left.suffix + right.prefix` as a crossing run.
8. The merged first character is `left.first_char`.
9. The merged last character is `right.last_char`.

## Algorithm

1. Build a segment tree over the original string.
2. For every query `(character, index)`:
   1. Follow the segment tree from the root to the leaf representing `index`.
   2. Replace that leaf's character with the new character.
   3. Recompute every ancestor using the merge operation.
   4. Read the root's `best` value.
   5. Append it to the answer.
3. Return all answers.

## Complexity

### Time Complexity

- Building the tree: **O(n)**.
- One point update: **O(log n)**.
- `q` updates: **O(q log n)**.
- Overall: **O(n + q log n)**.

### Space Complexity

**O(n)** for the segment tree.

## Edge Cases

- **Single-character string:** The answer is always `1`.
- **Entire string contains one character:** The root's `best` equals `n`.
- **Update changes a character to the same character:** The tree remains logically unchanged and still produces the correct answer.
- **Update breaks a long run:** The affected ancestors recompute their `best`, `prefix`, and `suffix`.
- **Update joins two runs:** The crossing case `left.suffix + right.prefix` captures the newly formed run.
- **Run crosses exactly at a segment boundary:** This is the central case handled by the merge function.
- **Empty string:** The implementation returns an empty list.

## Alternative Approaches

### Full Rescan After Every Update

- Simple.
- Time: **O(nq)**.
- Not suitable for large input.

### Segment Tree

- Point update: **O(log n)**.
- Global answer: **O(1)** after the update because it is stored at the root.
- Best fit for this problem.

### Other Dynamic Structures

A more specialized solution can maintain runs using ordered intervals or other balanced structures, but the segment tree gives a clean general-purpose solution and directly supports the required point-update/query pattern.

## Similar Problems

1. **LeetCode 307 — Range Sum Query - Mutable**  
   Segment tree/Fenwick tree with point updates, but the merge operation is simple addition.

2. **LeetCode 315 — Count of Smaller Numbers After Self**  
   Uses tree-based aggregation, though the query/update semantics differ.

3. **LeetCode 729 — My Calendar I**  
   Dynamic interval management; useful for thinking about maintaining changing ranges.

4. **LeetCode 715 — Range Module**  
   Dynamic range state; unlike this problem, the maintained structure represents intervals rather than a fixed segment tree summary.

5. **LeetCode 732 — My Calendar III**  
   Dynamic interval updates and global maximum; emphasizes maintaining an aggregate under updates.

6. **LeetCode 53 — Maximum Subarray**  
   A particularly important conceptual relative. A segment-tree solution stores boundary information such as prefix/suffix contributions so adjacent segments can be merged.

7. **LeetCode 1146 — Snapshot Array**  
   Another mutable-array problem, but its queries are historical rather than aggregate queries.

## Python Tips

- `zip(queryCharacters, queryIndices)` is a clean way to process paired query arrays.
- A list is convenient for a compact node representation, but a `dataclass` can improve readability when many fields are involved.
- Recursive segment-tree functions are natural for this problem.
- `TypeAlias` can document the intended node representation.
- `assert tree[1] is not None` is safe here, but the root is guaranteed to exist after `build`, so the assertion is not strictly necessary.

## Interview Discussion

### Why can't each node store only `best`?

Because the optimal run can cross the boundary.

For example, if the left segment ends with `aaa` and the right segment begins with `aa`, neither child alone knows that the combined run is `aaaaa`.

### Why do we need both prefix and suffix?

The prefix of the right segment and suffix of the left segment are exactly the two pieces that can join across a segment boundary.

### Why do we need first and last characters?

Without the boundary characters, we cannot determine whether the two boundary runs can be joined.

### What if updates were range updates?

A normal point-update segment tree would no longer be enough. The node state and update mechanism would need to be reconsidered, potentially involving lazy propagation depending on the operation.

### What makes this different from a standard sum segment tree?

The merge operation is problem-specific. Addition is associative and needs only one scalar. Here, the aggregate requires a richer summary containing boundary information.

## Personal Takeaways

1. **Segment trees are about designing the right node state, not memorizing one implementation.**
2. **For contiguous-run problems, boundary information is often as important as the internal optimum.**
3. **Ask what information a parent needs from each child before deciding what each node stores.**
4. **Point updates are a strong signal for segment trees when the answer can be recomputed from child summaries.**
5. **A crossing-boundary case should always be considered when merging contiguous segments.**
