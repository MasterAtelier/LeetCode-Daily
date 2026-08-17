# 1510. Stone Game IV

## Problem

- **Name:** Stone Game IV
- **Difficulty:** Hard
- **Category:** Dynamic Programming / Game Theory

## Core Pattern

### Win-Lose Game DP

Define `dp[x]` as whether the current player can force a win when `x` stones remain.

Recognition cues:
- Two players alternate turns.
- Both play optimally.
- A move transforms the current state into a smaller state.
- You need to determine whether the current player has a winning strategy.
- A state is winning if there is at least one move to a losing state.

Why the pattern applies:
If removing `k²` stones leaves `stones - k²` in a losing state for the opponent, the current player can make that move and win.

## Intuition

Think from the opponent's perspective.

For a given number of stones `stones`, try every legal square removal:

`1², 2², 3², ... <= stones`

If even one move sends the opponent to a losing state, the current state is winning.

Otherwise, every possible move gives the opponent a winning state, so the current state is losing.

The important recurrence is:

`dp[stones] = True` if there exists `k` such that `dp[stones - k²] == False`.

The base case is `dp[0] = False`: with zero stones, the player whose turn it is cannot move and therefore loses.

## Brute Force

### Idea

Use recursive game search without memoization. For every state, try every square number that can be removed and recursively solve the resulting state.

### Complexity

This repeatedly explores the same states and has exponential-time behavior in the worst case.

### Why it is inefficient

For example, many different sequences of square removals can lead to the same remaining number of stones. Without memoization, those states are solved repeatedly.

## Optimal Solution

### Key observations

1. Every move strictly decreases the number of stones.
2. Therefore, states can be solved from `0` upward.
3. `0` is losing.
4. A state is winning if it can move to any losing state.
5. A state is losing if every legal move leads to a winning state.

### Data Structures

A one-dimensional Boolean DP array:

`dp[x] = whether the current player wins with x stones remaining`.

### Algorithm Explanation

For every `stones` from `1` through `n`, enumerate all square numbers `k² <= stones`.

If `dp[stones - k²]` is `False`, mark `dp[stones]` as `True` and stop checking further moves.

If no such move exists, leave `dp[stones]` as `False`.

Return `dp[n]`.

## Algorithm

1. Create a Boolean array `dp` of length `n + 1`, initially all `False`.
2. Interpret `dp[0] = False` because no move is possible.
3. For each `stones` from `1` to `n`:
   - Start with `k = 1`.
   - While `k² <= stones`:
     - Check the state `stones - k²`.
     - If that state is losing, mark `dp[stones]` as winning and stop.
     - Otherwise increment `k`.
4. Return `dp[n]`.

## Complexity

There are approximately `sqrt(stones)` square choices for each state.

- **Time:** `O(n * sqrt(n))`
- **Space:** `O(n)`

For `n <= 10^5`, this is the standard DP complexity for the problem. citeturn0view0

## Edge Cases

- `n = 1`: Alice removes `1` and wins.
- `n = 2`: Alice can only remove `1`; Bob then removes the remaining `1`, so Alice loses.
- `n = 4`: Alice removes `4` immediately and wins.
- `n = 0` is not part of the problem constraints, but the DP base state must still represent it as losing.
- Perfect squares are immediately winning because the current player can remove the entire pile.

## Alternative Approaches

### Top-Down Memoization

Use recursive DFS with memoization.

This expresses the game recurrence naturally but has more recursion overhead in Python and does not improve the asymptotic complexity.

### Precomputed Square Numbers

Precompute all squares up to `n` and iterate through them for every state.

This can make the inner loop slightly cleaner, but the asymptotic complexity remains `O(n * sqrt(n))`.

## Similar Problems

1. **Stone Game** — two-player optimal-play reasoning, but uses a different game structure.
2. **Stone Game II** — game-state DP where the state contains both position and a changing move limit.
3. **Stone Game III** — game DP where players choose from a sequence and optimize score difference.
4. **Predict the Winner** — minimax-style DP over array intervals.
5. **Can I Win** — win/lose game DP with a much larger state space represented by used choices.
6. **Nim Game** — another winning/losing-state game where a mathematical characterization replaces DP.
7. **Divisor Game** — similar win/lose recurrence with legal moves determined by divisors.

## Python Tips

- A Boolean list is an efficient representation for win/lose DP.
- `k * k <= stones` avoids generating a square list and keeps the inner loop simple.
- `break` is important: once one winning move is found, the state is known to be winning.
- Python's `range` and list indexing make this bottom-up DP concise and readable.

## Interview Discussion

An interviewer may ask:

### Why is `dp[0]` false?

Because the player whose turn it is has no legal move and therefore loses.

### Why does finding one `False` child make the current state `True`?

The current player chooses the move. They only need one move that leaves the opponent in a losing position.

### Why is a state false when all children are true?

Every legal move would give the opponent a winning position, so the current player cannot force a win.

### Could you use recursion?

Yes. Memoization converts the repeated recursive subproblems into the same `O(n * sqrt(n))` state-transition complexity.

### Can the complexity be improved asymptotically?

The straightforward state-DP solution is `O(n * sqrt(n))`. Precomputing squares changes constants but not the asymptotic bound.

## Personal Takeaways

- In an impartial two-player game, ask: **Can I move to a losing state?**
- `win[state] = any(not win[next_state])`.
- Start from the terminal losing state and build upward when every move reduces the state.
- Game DP often becomes simple once the state is defined from the perspective of the player whose turn it is.
- Do not confuse “I can make a move” with “I can force a win”; the opponent also plays optimally.
