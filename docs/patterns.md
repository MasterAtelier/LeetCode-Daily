## Pattern: Interval Dynamic Programming with Minimax

### Recognition Signals

Look for problems where:

- Two players alternate turns.
- Both play optimally.
- Choices come from the ends of an array.
- The objective is to maximize one's own outcome.

### When to Use

Use this pattern when:

- The remaining game is completely described by a subarray.
- Each move leaves another interval.
- Future decisions depend only on the remaining interval.

### Reusable Template

1. Define DP on an interval `(l, r)`.
2. Let DP represent the best score difference for the current player.
3. Compute each available move.
4. Subtract the opponent's optimal result.
5. Take the maximum.
6. Memoize or tabulate.

### Common Variations

- Stone Game series
- Optimal Strategy for a Game
- Interval DP with costs
- Interval DP with merging

### Related Patterns

- Minimax
- Interval DP
- Game Theory DP

The key distinction is that Interval DP stores answers for contiguous subarrays, while generic Minimax may require much larger states.

### Problems Using This Pattern

- Predict the Winner
- Stone Game
- Stone Game VII
- Burst Balloons
- Remove Boxes