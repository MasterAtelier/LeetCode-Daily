# Find Missing Elements

## Problem

* **Name:** Find Missing Elements
* **Difficulty:** Easy
* **Category:** Hash Set / Membership Testing

## Core Pattern

### Main algorithmic pattern

Hash Set for O(1) membership testing.

### Recognition cues

Look for phrases such as:

* Missing elements
* Present in the array
* Find numbers within a range
* Existence lookup
* Fast membership checks

### Why the pattern applies

The task only requires determining whether each value in a known range exists. A hash set provides average O(1) lookups, eliminating the need for sorting.

---

## Intuition

First determine the smallest and largest values in the array. These define the complete original range. Store every number in a hash set, then iterate through the entire range and collect the values that are absent from the set.

---

## Brute Force

### Idea

For every number between the minimum and maximum values, linearly search the array to determine whether it exists.

### Complexity

* Time: O(n × R)
* Space: O(1)

where R = max(nums) − min(nums).

### Why it is inefficient

Each membership check scans the entire array.

---

## Optimal Solution

### Key observations

* The original range is completely determined by the minimum and maximum values.
* Only existence checks are required.
* Hash sets provide constant-time average membership testing.

### Data structures used

* Hash Set
* Output list

### Algorithm explanation

1. Insert every element into a hash set.
2. Find the minimum and maximum values.
3. Iterate from the minimum value to the maximum value (exclusive).
4. If a value is not present in the set, append it to the answer.
5. Return the answer.

---

## Algorithm

1. Build a hash set from the array.
2. Compute the minimum and maximum values.
3. Traverse every integer in the range.
4. Collect values missing from the set.
5. Return the collected list.

---

## Complexity

* **Time:** O(n + R)
* **Space:** O(n)

where R = max(nums) − min(nums).

---

## Edge Cases

* No missing numbers.
* Only two numbers in the array.
* Large gap between minimum and maximum.
* Missing numbers are consecutive.
* Input is completely unsorted.

---

## Alternative Approaches

1. Sort the array and identify gaps.

   * O(n log n) time
   * O(1) or O(n) space depending on sorting.

2. Boolean array (when value range is very small).

   * O(n + R) time
   * O(R) space.

---

## Similar Problems

* 217. Contains Duplicate
* 268. Missing Number
* 448. Find All Numbers Disappeared in an Array
* 128. Longest Consecutive Sequence
* 349. Intersection of Two Arrays
* 645. Set Mismatch

---

## Python Tips

* Use `set(nums)` for fast membership tests.
* `min(nums)` and `max(nums)` improve readability.
* List comprehensions can simplify filtering.

---

## Interview Discussion

Possible follow-up questions:

* Can this be solved without extra space?
* What if duplicate values are allowed?
* What if the value range is extremely large?
* What changes if the array is already sorted?

---

## Personal Takeaways

* Separate ordering problems from membership problems.
* Use a hash set whenever only existence checks are needed.
* Avoid sorting unless ordering information is required.
* Identify the minimum information needed to solve the problem.
