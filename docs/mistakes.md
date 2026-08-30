## Predict the Winner

Date: 2026-08-02

### Mistakes

#### 1. Used OR for both players

**Classification:** Logic

- Initially modeled Player B as trying to help Player A by using OR.
- Forgot that Player B plays optimally against Player A.
- Correct logic:
  - Player A → OR
  - Player B → AND

**Lesson**

Always identify whether each player is maximizing or minimizing the objective.

---

#### 2. Mutated the turn variable before deciding the result

**Classification:** Implementation

- Flipped `curr_player_A` before determining whether to use OR or AND.
- This reversed the decision logic.

**Lesson**

Avoid mutating state variables unnecessarily. Prefer passing the updated value directly to recursive calls.

---

#### 3. Chose an unnecessarily large memoization state

**Classification:** Complexity

Initial state:

```
(i, j, turn, scoreA, scoreB)
```

This prevented effective memoization because very few states repeated.

**Lesson**

Always ask:

> "What information actually determines the answer?"

The answer depended only on `(i, j)`.

---

#### 4. Tried to use a list inside a dictionary key

**Classification:** Python-specific

Attempted to include `nums` in the memoization state.

Lists are mutable and unhashable.

**Lesson**

Dictionary keys must be hashable.

Use tuples or omit immutable shared inputs from the state.

## Stone Game III

**Date:** 2026-08-03

### Mistakes

#### 1. Tried a greedy strategy for an optimal-play game

**Classification:** Logic

**What I did**

At each turn, I chose the option (taking 1, 2, or 3 stones) with the largest immediate sum.

**Why it was incorrect**

The objective is to maximize the final score difference after both players play optimally, not the immediate gain. A locally optimal move can allow the opponent to obtain an even larger advantage.

**Why I might have thought it was correct**

The problem asks to maximize the score, which can make it tempting to optimize the current move instead of the entire game.

**How to recognize this mistake in future problems**

Whenever two players take turns and both play optimally, question any greedy approach first.

**How to avoid repeating it**

Think in terms of game states and future consequences. Consider minimax or score-difference DP before attempting greedy.

---

#### 2. Chose an incorrect DP state

**Classification:** Data Structure

**What I did**

Initially memoized using `(sumA, sumB)` and later `(index, currentPlayer)`.

**Why it was incorrect**

The future of the game depends only on the remaining stones. Previous scores do not affect future decisions, and the current player is already implicit in the score-difference recurrence.

**Why I might have thought it was correct**

I modeled the game using the actual scores instead of identifying the minimal state needed for future computation.

**How to recognize this mistake in future problems**

Ask whether each variable in the DP state can change the remaining subproblem. If removing it does not change future decisions, it should not be part of the state.

**How to avoid repeating it**

Define the DP state as the smallest amount of information required to uniquely determine the remaining problem.

---

#### 3. Generated invalid transitions

**Classification:** Edge Case

**What I did**

Initially represented impossible moves using placeholder values instead of only exploring valid moves.

**Why it was incorrect**

DP transitions should correspond only to legal game moves. Exploring illegal transitions complicates the recurrence and can introduce subtle bugs.

**How to recognize this mistake in future problems**

Whenever a move has constraints, generate only valid transitions instead of filtering them afterward.

**How to avoid repeating it**

Iterate only over legal choices using a loop with boundary checks.

### Lessons

- In optimal-play games, think about **future advantage**, not immediate gain.
- The best DP state is usually the smallest state that completely describes the remaining subproblem.
- Score-difference DP often eliminates the need to explicitly track players or individual scores.


## Remove Methods From Project

**Date:** 2026-08-05

### Mistakes

#### 1. Used Union-Find instead of graph traversal
- **Category:** Data Structure
- **Issue:** Treated directed reachability as undirected connectivity.
- **Why it seemed reasonable:** Union-Find is commonly used for grouping connected nodes.
- **Lesson:** Reachability in directed graphs requires BFS/DFS, not Union-Find.

#### 2. Converted directed edges into undirected edges
- **Category:** Logic
- **Issue:** Added reverse edges that do not exist.
- **Lesson:** Preserve edge direction unless the problem explicitly states the graph is undirected.

#### 3. Explored only one or two levels of neighbors
- **Category:** Logic
- **Issue:** Missed methods reachable through longer paths.
- **Lesson:** When a problem says "directly or indirectly", perform a complete graph traversal.

#### 4. Marked nodes as visited too late during BFS
- **Category:** Implementation
- **Issue:** Could enqueue the same node multiple times.
- **Lesson:** Mark nodes visited when enqueueing them.

#### 5. Initially forgot the incoming-edge validation
- **Category:** Logic
- **Issue:** Identified suspicious methods correctly but didn't verify whether they could be removed.
- **Lesson:** After finding a component, carefully read the problem for any additional validity conditions.

## Shortest and Lexicographically Smallest Beautiful String
Date: 2026-08-26

### Mistakes

1. **Used an invalid sentinel boundary without handling it during candidate comparison**

- **Classification:** Logic / Implementation
- **What I did:** Initialized `end = -1`, then compared candidates using `curr_len < end - start + 1`.
- **Why it was incorrect:** With `start = 0` and `end = -1`, the stored length is `0`. A valid candidate has positive length, so `curr_len < 0` is never true and `curr_len == 0` is also false. Consequently, the first valid candidate was never stored.
- **Why I might have thought it was correct:** `end = -1` is a common sentinel for "no answer yet", but the sentinel must be handled before ordinary length comparisons.
- **How to recognize this in future problems:** Whenever an answer uses a sentinel such as `-1`, `None`, or an empty structure, check the first candidate explicitly rather than applying normal comparison logic to the sentinel.
- **How to avoid repeating it:** Use `if end == -1 or ...` when evaluating the first candidate.

### Root Cause
The sliding-window logic itself was correct. The failure came from **answer initialization**, not from the window invariant.

## Removing Minimum and Maximum From Array

**Date:** 2026-08-30

### Mistakes

#### 1. Logic — Independently adding minimum and maximum deletion costs

Initially, the solution calculated the minimum deletion cost for the maximum and minimum independently and added them.

The mistake was that both target elements can sometimes be removed by the **same deletion operations**.

The correct approach is to consider the three complete strategies rather than independently optimizing each element.

#### 2. Logic — Using the wrong boundary for right-side deletion

The first corrected formula used:

```
n - right
```

for deleting both elements from the right.

This is incorrect because when deleting exclusively from the right, we must reach the **leftmost** target element.

The correct cost is:

```
n - left
```

**Why I might have thought it was correct:**

`right` is the rightmost relevant index, so it can feel intuitive to calculate the distance from that index to the right boundary. However, reaching `right` does not necessarily remove the earlier target at `left`.

**How to recognize this mistake in future problems:**

When calculating a boundary-removal cost, ask:

> Which target element must the deletion process reach for ALL required elements to have been removed?

**How to avoid repeating it:**

Draw the indices and explicitly mark the deleted interval before writing the formula.

### Lessons

- Do not independently optimize operations when operations can overlap.
- For boundary problems, reason about the entire deleted interval.
- Identify the exact target boundary that each strategy must reach.
- Draw a small index diagram when an off-by-one or boundary choice is unclear.

### How to avoid in future

For problems involving deletion from array ends:

1. Mark all required target indices.
2. Sort/normalize their positions.
3. Draw each possible deletion strategy.
4. Calculate the number of elements removed by each strategy.
5. Take the minimum.