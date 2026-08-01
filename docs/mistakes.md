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