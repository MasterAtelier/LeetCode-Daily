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

---

## Pattern: XOR-Based Maximum-Length Selection

### Recognition Signals

Look for problems involving:

- Longest subsequence with an XOR constraint
- Maximum number of elements while satisfying a bitwise condition
- Removing the minimum number of elements
- XOR of the entire array
- Conditions involving XOR being zero or non-zero

Typical clues:

- "Longest subsequence..."
- "Non-zero XOR"
- "Bitwise XOR"
- "Remove elements..."
- "Maximum length..."

---

## When to Use

Use this pattern when:

1. The objective is to maximize the number of retained elements.
2. The constraint depends only on the XOR of selected elements.
3. The XOR of the entire array can be computed directly.
4. Removing a single element has a predictable effect on the XOR.

---

## Key XOR Identities

### Cancellation

    x ^ x = 0

### Identity

    x ^ 0 = x

### Removing an Element

If:

    total_xor = XOR(all elements)

then removing `x` gives:

    remaining_xor = total_xor ^ x

Therefore, if:

    total_xor = 0

then:

    remaining_xor = x

This is the key observation behind the problem.

---

## Reusable Template

1. Compute the XOR of all elements.
2. Check whether the complete array satisfies the condition.
3. If it does, return the full length.
4. If it does not, determine whether removing one element can satisfy the condition.
5. Prove that the resulting length is achievable.
6. Prove that no longer answer is possible.
7. Handle the degenerate case where no valid subsequence exists.

---

## Common Variations

### Full XOR is already valid

Return the full array length.

### Full XOR is invalid but one removal fixes it

Return:

    n - 1

### No non-zero element exists

Return `0`.

### XOR target instead of non-zero

The problem may require a more sophisticated XOR-state approach.

---

## Related Patterns

### XOR Cancellation

Useful when values appear repeatedly and pairs cancel.

### Bitmask / Bit Manipulation

Useful when the condition depends on individual bits.

### Prefix XOR

Useful when the problem involves XOR over subarrays.

### XOR Linear Basis

Useful when maximizing or representing XOR values across many choices.

---

## Problems Using Similar Ideas

- Single Number
- Missing Number
- Maximum XOR of Subsequences
- Maximum XOR for Each Query
- XOR Queries of a Subarray
- Single Number II
- Single Number III

---

## Interview Recognition Rule

When you see:

> "Maximum/longest subsequence with a bitwise XOR condition"

ask immediately:

> "What is the XOR of the entire array, and what happens if I remove exactly one element?"

This question can turn an exponential subsequence problem into a linear scan.


## Pattern: Variable-Size Sliding Window with Frequency Constraint

### Recognition Signals

Look for problems containing phrases such as:

- "Longest subarray"
- "Longest substring"
- "At most K"
- "At most K occurrences"
- "Each element appears at most K times"
- A contiguous range with a constraint that can be maintained incrementally

### When to Use

Use this pattern when:

- The problem operates on a contiguous subarray or substring.
- The goal is to maximize or minimize the window length.
- The validity of a window can be maintained using incremental state.
- Moving the left boundary forward can restore validity after the right boundary makes the window invalid.
- Both pointers can move monotonically from left to right.

### Reusable Template

1. Initialize `left` at the beginning of the sequence.
2. Initialize the state needed to determine whether the current window is valid.
3. Expand the window by moving `right`.
4. Update the state with the new element.
5. While the window violates the constraint:
   - Remove the element at `left` from the state.
   - Move `left` forward.
6. Record the best valid window.
7. Continue until `right` reaches the end.

### Common Variations

- At most `K` occurrences of each value.
- At most `K` distinct values.
- At most `K` violations.
- Longest window containing only unique values.
- Minimum-size window satisfying a condition.
- Frequency-map window.
- Hash-set window.

### Related Patterns

- Frequency Counting (Hash Map)
- Hash Set for Membership Testing
- Fixed-Size Sliding Window
- Prefix Sum + Hash Map
- Two Pointers

### Problems Using This Pattern

- 2958. Length of Longest Subarray With at Most K Frequency
- 3090. Maximum Length Substring With Two Occurrences
- 3. Longest Substring Without Repeating Characters
- 904. Fruit Into Baskets
- 1004. Max Consecutive Ones III
- 340. Longest Substring with At Most K Distinct Characters
- 159. Longest Substring with At Most Two Distinct Characters
- 424. Longest Repeating Character Replacement
- Minimum Window Substring

## Pattern: Segment Tree with Boundary-Aware Custom Merge

### Recognition Signals

Look for problems with combinations such as:

- "After each update, return..."
- "Update index `i`..."
- "Change this character/value..."
- "Longest contiguous..."
- "Maximum subarray/run/segment..."
- Many **point updates** on a fixed array or string.
- The answer can be represented as an aggregate of adjacent segments.
- A valid answer may cross the boundary between two independently summarized segments.

A particularly strong signal is:

> **Point updates + repeated aggregate queries + a contiguous property whose answer can cross segment boundaries.**

### When to Use

Use this pattern when:

- The underlying sequence length is fixed.
- Updates modify individual positions.
- Queries ask for a global or range aggregate after updates.
- Recomputing the entire sequence after every update is too expensive.
- Two neighboring segments can be combined using a fixed merge rule.
- Each segment can be summarized with a small amount of information.

### Reusable Template

1. Define the smallest summary that completely describes what the parent needs from a segment.
2. Identify the leaf representation for one element.
3. Define a merge operation:
   - Combine the left and right summaries.
   - Handle values entirely inside either child.
   - Explicitly handle answers crossing the boundary.
4. Build the segment tree bottom-up or recursively.
5. For a point update:
   - Replace the corresponding leaf.
   - Recompute summaries along the path to the root.
6. Read the required aggregate from the root or perform a range query.

### Common Variations

- Range sum with point updates.
- Range minimum/maximum with point updates.
- Longest equal-character run after point updates.
- Maximum subarray sum with point updates.
- Longest prefix/suffix satisfying a property.
- Maintaining counts plus boundary information.
- Range queries where the answer depends on adjacent elements.

### Related Patterns

- **Fenwick Tree:** Prefer when the aggregate is suitable for prefix/range operations such as sums and point updates.
- **Standard Segment Tree:** Same tree structure, but the node summary is usually a simple scalar.
- **Lazy Segment Tree:** Use when updates affect ranges rather than individual points.
- **Divide and Conquer:** The merge concept is similar, but segment trees extend it to repeated dynamic updates.
- **Monoid/Associative Merge:** The most general viewpoint: design a compact summary and an associative merge operation.

### Important Variation: Boundary-Aware State

For longest contiguous runs, storing only the best answer in each segment is insufficient.

A segment should expose:

- Its total length.
- Longest valid prefix.
- Longest valid suffix.
- Longest valid run anywhere inside.
- First boundary value.
- Last boundary value.

The parent can then detect whether the optimal run crosses the midpoint.

### Problems Using This Pattern

- **2213. Longest Substring of One Repeating Character** — Maintain longest equal-character run after point updates.
- **53. Maximum Subarray** — A segment-tree formulation can maintain total sum, best prefix, best suffix, and best subarray sum.
- **307. Range Sum Query - Mutable** — Simpler segment-tree merge using addition.

## Pattern: Game Theory + Modular Arithmetic + State Compression

### Recognition Signals

Look for phrases or conditions involving:

- "sum is divisible by..."
- "remainder"
- "modulo"
- Two players making alternating moves
- Losing or winning based on a cumulative value
- Many values that behave identically under a modulus
- A game where the exact values appear much more detailed than the actual win condition requires

A strong signal is:

> The outcome depends only on a value modulo a small integer.

### When to Use

Use this pattern when:

1. The game state depends on a cumulative sum or difference.
2. Only the remainder of that quantity matters.
3. Different input values with the same remainder are strategically equivalent.
4. The number of possible residues is small enough to reason about directly.

For Stone Game IX, there are only three relevant states: `0`, `1`, and `2` modulo 3.

### Reusable Template

1. Identify the mathematical property that determines the game outcome.
2. Determine the smallest state needed to represent that property.
3. Map each input value into that state.
4. Count or otherwise compress equivalent states.
5. Analyze the game on the compressed state space.
6. Derive the winning condition from optimal play.
7. Validate the condition against brute force for small inputs.
8. Implement the final condition using the compressed representation.

### Common Variations

#### Different modulus

The same idea may apply when the game depends on modulo `k` instead of modulo 3.

#### State-frequency counting

If elements with the same state are interchangeable, replace the original sequence with frequencies.

#### Game + invariant

Sometimes a mathematical invariant determines the winner without requiring explicit simulation.

#### Game + DP

If the compressed state is still too large for a direct mathematical characterization, use memoization or dynamic programming over the compressed state.

### Related Patterns

#### Minimax / Game DP

Use when both players optimize their outcome and the future depends on previous choices.

**Distinguish it from this problem:** Stone Game IX can be reduced far enough that explicit minimax is unnecessary.

#### Bitmask DP

Use when the identity of remaining elements matters and `n` is small.

**Distinguish it from this problem:** Here, individual identities do not matter; only residue counts matter.

#### Greedy

Use when a locally optimal move can be proven to preserve global optimality.

**Distinguish it from this problem:** The final solution is not a generic greedy simulation; it is a mathematical characterization of the game.

#### Invariant-based reasoning

Use when the game outcome is controlled by a quantity that remains constrained under every move.

**Distinguish it from this problem:** The modulo-3 state is the central invariant.

### Problems Using This Pattern

- **Stone Game IX** — reduce values to residues modulo 3 and reason about residue counts.
- **Nim** — reduce a game to a mathematical invariant.
- **Divisor Game** — game outcome collapses to a mathematical property.
- **Can I Win** — game-state compression with memoization, although the state representation is fundamentally different.
- **Stone Game III** — game theory plus DP rather than a direct modular characterization.

### One-Minute Recognition Rule

When a game says:

> "Players take numbers, and something happens when the running sum reaches a divisibility/modulo condition."

immediately ask:

> **Can I replace every number by its remainder and count equivalent residues?**

That question can turn an exponential game simulation into an O(n) counting solution.

---

# Pattern: Interval DP with a Monotonic Partition Boundary

## Recognition Signals
Look for:

- "split the array"
- "partition the interval"
- "left sum / right sum"
- "choose the smaller side"
- "maximize the score after splitting"
- A contiguous interval with a split point.
- A naive `O(n^3)` interval DP.
- A partition condition whose boundary moves monotonically.

## When to Use
Use this optimization when:

1. The problem is naturally interval DP.
2. The transition depends on a boundary condition.
3. The boundary can be proven monotonic as one endpoint changes.
4. Array properties, such as positive values, guarantee the monotonicity.

Always prove the monotonicity before replacing binary search with a moving pointer.

## Reusable Template

1. Define the interval DP state.
2. Express the transition using a split boundary.
3. Build prefix sums.
4. Identify the largest/smallest split satisfying the condition.
5. Prove that this boundary moves in one direction.
6. Reuse the previous boundary with a pointer.
7. Advance the pointer only when the next position remains valid.
8. Precompute prefix/suffix aggregates for transition regions.
9. Update the DP state in constant time.

## Common Variations

- Binary-search boundary -> monotonic pointer.
- Prefix maximum -> suffix maximum.
- Two-sided partition conditions.
- Equality requiring both transitions.
- Monotonic queue/deque for sliding-window aggregates.
- Divide-and-conquer DP optimization when the optimal split is monotonic.
- Knuth optimization when its required interval conditions hold.

## Related Patterns

### Standard Interval DP
Try every split explicitly.

- Usually `O(n^3)`.
- Easy to derive.
- Excellent as a brute-force correctness oracle.

### Interval DP + Binary Search
Use when the split condition is monotonic but a pointer cannot conveniently be reused.

- Often `O(n^2 log n)`.

### Monotonic Pointer Optimization
Use when neighboring states have boundaries that only move forward or backward.

- Can reduce `O(n^2 log n)` to `O(n^2)`.

### Divide-and-Conquer DP Optimization
Uses monotonicity of the optimal split itself. Its proof and recurrence requirements differ from this problem.

## Problems Using This Pattern

- **Stone Game V (LeetCode 1563)** — partition by comparing left and right sums; the boundary is monotonic for fixed `i`.
- **Stone Game VII** — interval DP with prefix sums, but a different transition.
- **Burst Balloons** — interval DP over split points, useful for contrasting standard split enumeration.
- **Minimum Cost to Cut a Stick** — interval DP over partition points.

## Pattern: Local State Compression + Greedy Selection

## Recognition Signals

Look for problems where:

- The input is divided into independent components such as rows, intervals, or groups.
- Most of the input has a predictable default contribution.
- Only a small subset of positions affects the answer.
- There are only a few valid configurations per component.
- Candidate configurations overlap, requiring a compatibility decision.

Typical phrases include:

- "maximum number of groups"
- "reserved positions"
- "place as many as possible"
- "non-overlapping"
- "available positions"
- "each row independently"

## When to Use

Use this pattern when each component can be solved independently and the component has a small finite state space.

The key steps are:

1. Identify the independent components.
2. Determine the default contribution of an unconstrained component.
3. Compress constrained components to only the information that matters.
4. Enumerate the small set of valid local configurations.
5. Resolve overlaps with a greedy or constant-size compatibility rule.

## Reusable Template

1. Partition the input into independent units.
2. Compute the contribution from units with no constraints.
3. For each constrained unit:
   - Keep only relevant state.
   - Define the candidate configurations.
   - Determine which candidates are available.
   - Select a maximum compatible subset.
4. Add all local contributions.

## Common Variations

- **Bitmask state:** Encode a small number of positions as bits.
- **Set state:** Store occupied positions and test candidate groups.
- **Interval compatibility:** Select non-overlapping intervals greedily.
- **Small DP state:** Use DP when local configurations cannot be resolved by a simple greedy rule.
- **Precomputed patterns:** Map each small state to its optimal answer.

## Related Patterns

- **Greedy:** Use when a locally optimal compatible choice can be proven to preserve global optimality.
- **Bitmasking:** Useful when the number of relevant binary positions is small.
- **Hash Map / Grouping:** Useful for processing only constrained components.
- **Interval Scheduling:** Similar when candidate configurations overlap and must be selected compatibly.
- **Dynamic Programming:** Prefer this when local choices have interactions that greedy selection cannot resolve.

## Problems Using This Pattern

- **LeetCode 1386 — Cinema Seat Allocation:** Three possible family blocks per occupied row.
- **LeetCode 605 — Can Place Flowers:** Local placement with spacing constraints.
- **LeetCode 435 — Non-overlapping Intervals:** Select compatible intervals greedily.
- **LeetCode 452 — Minimum Number of Arrows to Burst Balloons:** Overlapping intervals and greedy compatibility.
- **LeetCode 1893 — Check if All the Integers in a Range Are Covered:** Fixed-range coverage and compact state reasoning.