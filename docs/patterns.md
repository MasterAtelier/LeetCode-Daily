## Pattern: Interval Dynamic Programming with Minimax

### Recognition Signals

Look for problems where:

- Two players alternate turns.
- Both players play optimally.
- The game state is completely described by a contiguous interval (subarray).
- Each move shrinks the interval by making one of a few possible choices.
- The objective is to maximize your own outcome or determine whether the first player wins.
- Choices are often made from the ends of an array, but may also involve other interval-based decisions.

---

### When to Use

Use this pattern when:

- The remaining game depends only on an interval `(l, r)`.
- Every move transitions to another interval.
- Both players have complete information and play optimally.
- The outcome of the current state depends only on the optimal result of smaller intervals.

---

### Key Insight

Instead of explicitly tracking:

- Player turns
- Player 1's score
- Player 2's score

track only the **maximum score difference** the current player can achieve.

```
Score Difference = Current Player's Score − Opponent's Score
```

If the current player takes a move worth `gain`, the opponent then becomes the current player on the remaining interval.

Therefore,

```
Current Advantage = gain − Opponent's Best Advantage
```

This observation compresses the DP state to just the interval `(l, r)`.

---

### Reusable Template

1. Define `dp(l, r)` as the maximum score difference the current player can achieve on interval `(l, r)`.
2. If only one element remains, return its value.
3. Enumerate every legal move.
4. For each move:
   - Add the immediate gain.
   - Subtract the opponent's optimal score difference on the resulting interval.
5. Take the maximum over all possible moves.
6. Memoize (top-down) or tabulate (bottom-up).
7. If `dp(0, n-1) > 0`, Player 1 wins.

---

### Common Variations

#### Two-player interval games

- Predict the Winner
- Stone Game
- Stone Game II
- Stone Game III
- Stone Game VII
- Coins in a Line
- Optimal Strategy for a Game (GFG)

#### Other Interval DP problems (not Minimax)

- Burst Balloons
- Remove Boxes
- Minimum Cost to Merge Stones
- Matrix Chain Multiplication
- Palindrome Removal

---

### Related Patterns

#### Interval DP

Stores answers for contiguous subarrays. May or may not involve multiple players.

#### Minimax

Models optimal decisions in adversarial games. States are not necessarily intervals.

#### Game Theory DP

General dynamic programming for optimal-play games.

#### Memoized DFS

A common implementation technique for interval DP.

**Distinguishing Feature**

This pattern combines **Interval DP** with **Minimax**, allowing the entire game state to be represented using only the interval `(l, r)` while the minimax behavior is captured through the score-difference recurrence.

---

### Problems Using This Pattern

| Problem | Variation |
|---------|-----------|
| Predict the Winner | Classic score-difference interval DP |
| Stone Game | Same pattern (problem-specific mathematical shortcut exists) |
| Stone Game II | Variable number of piles can be taken |
| Stone Game III | Up to three choices per move |
| Stone Game VII | Score gained depends on remaining sum |
| Coins in a Line | Classical interval game DP |
| Optimal Strategy for a Game (GFG) | Classical interval minimax DP |

---

### Interview Tips

- First identify whether the game state can be represented solely by an interval.
- Avoid tracking both players' scores independently.
- Ask whether **score difference** is sufficient to represent the state.
- Many two-player DP problems become significantly simpler once the correct state is defined.
- Always look for opportunities to reduce unnecessary state variables before writing the recurrence.



## Pattern: Minimax DP (Score Difference)

### Recognition Signals

Look for problems involving:

- Two players taking turns.
- Both players play optimally.
- Determine the winner.
- Each move offers a small number of choices.
- Maximize your own score while minimizing your opponent's.

### When to Use

Use this pattern when:

- The remaining game depends only on the current state.
- Both players have perfect information.
- The game has no randomness.
- Tracking the score difference is simpler than tracking both players' scores.

### Reusable Template

1. Define `dp(state)` as the maximum score difference the current player can achieve.
2. Enumerate every legal move.
3. Compute the immediate gain.
4. Subtract the opponent's optimal score difference from the next state.
5. Return the maximum over all legal moves.

### Common Variations

- Taking 1 to K items.
- Picking from either end of an array.
- Interval game DP.
- Recursive memoization.
- Bottom-up DP.

### Related Patterns

- Minimax Search
- Interval DP
- Dynamic Programming on Arrays

### Problems Using This Pattern

- 1406. Stone Game III
- 877. Stone Game
- 1140. Stone Game II
- 1690. Stone Game VII
- 486. Predict the Winner
- 464. Can I Win

### Pattern: Reachability + Component Validation

#### Recognition Signals

- "Starting from node X"
- "Directly or indirectly"
- "Reachable methods"
- "Remove all reachable nodes"
- "Validate whether the group can be removed"

#### Template

1. Traverse from the given source.
2. Record the reachable set.
3. Validate the set against the problem's additional constraints.
4. Produce the final answer.

#### Variation

Many graph problems consist of:
- Discover a component.
- Validate the component.
- Answer based on validation.

## Greedy Suffix Reconstruction with Prime Factor Accounting

### Recognition Signals

- Lexicographically smallest valid number
- Product divisibility
- Large numeric strings
- Prime factor constraints

### When to Use

Use when each digit contributes independent prime factors and the goal is to construct the smallest valid number without enumerating candidates.



### New Observation

Maintaining prefix prime-factor counts enables O(n) greedy reconstruction after a single right-to-left scan.


## Pattern: Greedy Subsequence Construction with Suffix Feasibility

### Recognition Signals

Look for problems where:

* You need to construct a subsequence from a string or array.
* The answer must be **lexicographically smallest** or use the earliest possible indices.
* You are allowed a limited number of deviations, such as:

  * At most one mismatch.
  * At most `K` mismatches.
  * A limited number of substitutions.
* A greedy choice may be valid only if the remaining target can still be completed.
* The problem asks for indices rather than only the resulting string.

### When to Use

Use this pattern when:

* You want the earliest possible index at every step.
* Selecting an element now can affect whether the remaining target is achievable.
* The remaining portion can be checked efficiently using precomputed suffix information.
* A small amount of state, such as `used_mismatch`, represents the special operation already consumed.

### Key Insight

For a lexicographically smallest index sequence, always prefer the earliest possible index.

However, an early choice is safe only if it does not make the remainder impossible.

Separate choices into two cases:

1. **Exact match**

   If the current character matches the next required target character, take it immediately.

2. **Allowed mismatch**

   If it does not match, use the mismatch only when the remaining suffix can still match the remaining target exactly.

This leads to the general strategy:

```text
Choose the earliest feasible index.
```

The important word is **feasible**.

A suffix preprocessing pass allows feasibility to be checked in O(1) during the greedy scan.

### Reusable Template

1. Precompute information about how much of the target can be matched by every suffix of the source.
2. Scan the source from left to right.
3. Maintain the current position in the target.
4. If the current element matches:

   * Select it.
   * Advance the target position.
5. Otherwise:

   * Check whether the limited special operation is still available.
   * Check whether selecting the current element leaves a feasible suffix.
   * If both conditions hold, select it and consume the special operation.
6. Continue until the target is completely constructed or the source is exhausted.
7. Return the constructed sequence if the target was completed.

### Common Variations

#### At most one mismatch

One special operation can be used during the greedy construction.

#### At most K mismatches

Maintain a mismatch count instead of a boolean state.

#### Different substitution costs

The feasibility condition may track the remaining available cost rather than simply whether a mismatch is available.

#### Lexicographically smallest subsequence

The special operation may not be present; suffix feasibility is still useful when an early greedy choice can make completion impossible.

### Related Patterns

#### Greedy Subsequence Matching

Choose the earliest possible matching elements.

**Difference:** Basic subsequence matching does not normally need a feasibility check because every selected element must match exactly.

#### Greedy + Feasibility Check

Make the locally optimal choice only when the remaining problem remains solvable.

**Difference:** The feasibility information may come from suffix preprocessing, dynamic programming, or another data structure.

#### Prefix/Suffix Preprocessing

Precompute information from one direction and use it while making decisions in the opposite direction.

**Difference:** Prefix/suffix preprocessing is a technique; this pattern combines it specifically with greedy subsequence construction.

#### Lexicographically Smallest Construction

Repeatedly choose the smallest/earliest option that can lead to a valid complete answer.

### Problems Using This Pattern

| Problem                                                  | Variation                                              |
| -------------------------------------------------------- | ------------------------------------------------------ |
| 3302. Find the Lexicographically Smallest Valid Sequence | At most one character mismatch with suffix feasibility |
| 524. Longest Word in Dictionary Through Deleting         | Greedy subsequence matching                            |
| 392. Is Subsequence                                      | Basic subsequence feasibility                          |
| 1673. Find the Most Competitive Subsequence              | Lexicographically smallest subsequence                 |
| 316. Remove Duplicate Letters                            | Lexicographically smallest valid reconstruction        |

### Interview Tips

* When asked for the **lexicographically smallest sequence of indices**, think **earliest feasible choice**, not merely earliest choice.
* Ask: **"If I take this element now, can I still finish the target?"**
* If that question must be answered repeatedly, look for prefix/suffix preprocessing.
* Separate **optimization** from **feasibility**:

  * Greedy determines which choice is best.
  * Suffix information determines whether that choice is safe.
* A common mistake is to spend the allowed mismatch at the first mismatch without checking whether the remaining target can still be matched.
* When a problem allows only a small number of exceptional operations, explicitly track whether those operations have already been consumed.


## Variation: Game DP with a Dynamic Move-Bound State

### Recognition Signals

A two-player game where:

* Players alternate optimally.
* The remaining input is a suffix or smaller state.
* The number of elements that can be taken depends on a variable from the previous move.
* That variable changes after every move.

Typical signal:

> "You may take between 1 and `K` elements, and `K` changes based on how many you took."

### Key Observation

The move-bound variable is part of the DP state.

For Stone Game II:

`state = (position, M)`

where `M` determines the legal range:

`1 <= X <= 2M`

After taking `X`:

`M = max(M, X)`

### Reusable Template

1. Identify the smallest state describing the remaining game.
2. Include every variable that affects future legal moves.
3. Enumerate every legal move.
4. Transition to the opponent's state.
5. Express the current player's result using the opponent's optimal result.
6. Memoize the state.

For additive rewards:

`current_result = total_remaining - opponent_result`

### Important Distinction

This is different from ordinary interval game DP.

In interval DP, the state is often:

`(left, right)`

In Stone Game II, the state is:

`(position, move_bound)`

The second dimension is not a boundary of the input. It is a **dynamic game parameter** created by previous decisions.

### Problems Using Related Ideas

* 1140. Stone Game II
* 1406. Stone Game III
* 1510. Stone Game IV
* 486. Predict the Winner
* 1690. Stone Game VII

### Interview Insight

When a game says that the number of choices available on the next turn depends on the current move, immediately ask:

> **What variable controls my next legal moves, and does it need to become part of my DP state?**

That question often reveals the correct state definition before any recurrence is written.

## Pattern: Win-Lose Dynamic Programming for Two-Player Games

### Recognition Signals

Look for problems where:

- Two players alternate turns.
- Both players play optimally.
- A state has a finite set of legal moves.
- Every move transitions to a smaller or already-solvable state.
- The question asks whether the current player can force a win.
- A player loses when no legal move is available.

Typical language:
- "return true if the first player wins"
- "both players play optimally"
- "the player unable to make a move loses"
- "can the current player force a win?"

### When to Use

Use this pattern when the game can be represented by a manageable state and each move transitions to another state whose outcome can be computed.

For a state `S`:

- `S` is **winning** if there exists a legal move to a losing state.
- `S` is **losing** if every legal move leads to a winning state.

For Stone Game IV, the state is simply the number of remaining stones.

### Reusable Template

1. Identify the complete game state.
2. Identify terminal states.
3. Mark terminal losing/winning states.
4. Enumerate legal moves from each state.
5. Mark a state winning if at least one move reaches a losing state.
6. Otherwise mark it losing.
7. Build states in an order where all successor states are already known.

### Common Variations

- **1D state:** remaining stones, score, position, or amount.
- **Multi-dimensional state:** position plus a changing move limit.
- **Score-based game DP:** store the best score difference instead of a Boolean.
- **Interval game DP:** state is a contiguous interval.
- **Bitmask game DP:** state represents which choices/items have already been used.
- **Memoized minimax:** compute only states reached by recursive play.

### Related Patterns

- **Minimax DP:** useful when the objective is an actual score/value rather than only win/lose.
- **Interval DP:** use when the remaining game state is a subarray or interval.
- **Bitmask DP:** use when the state depends on a subset of used choices.
- **Mathematical game theory:** use when the winning/losing states have a direct mathematical characterization, eliminating the need for DP.

### Problems Using This Pattern

- Stone Game IV
- Nim Game
- Divisor Game
- Can I Win
- Stone Game III
- Stone Game II
- Predict the Winner

### New Observation from Stone Game IV

The most reusable mental model is:

> **Winning = there exists a move to losing.**

This is often easier to reason about than directly trying to describe how a player wins. Start with the state where no move is possible, label it losing, and propagate the labels backward.
