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