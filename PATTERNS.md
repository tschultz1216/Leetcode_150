# Pattern Reference

A catalogue of algorithm patterns, their tells, and when to use them. Built from problems solved in this repo — updated as new patterns are encountered.

---

## Greedy

Use greedy when the best local decision at each step is never wrong in hindsight. You never need to backtrack or revise a previous choice.

**Recognition checklist — all should hold:**
1. **No revisiting** — the locally optimal choice now is still optimal later
2. **Single running value** — solution reduces to one variable moving in one direction (max grows, min shrinks, sum accumulates)
3. **Linear structure** — input is processed forward without branching paths that need comparing
4. **Yes/no, max, or min** — not enumerating all solutions or paths

**Greedy is NOT Dijkstra's.** Dijkstra's finds shortest path in a weighted graph using a priority queue — O(n log n) time, O(n) space. Greedy here is O(n) time, O(1) space — no graph, no queue, no cost tracking.

| Tell | Pattern | Example |
|---|---|---|
| "single day to buy, different day to sell" | Track running minimum + max profit | Best Time to Buy and Sell Stock |
| "buy and sell multiple times" | Sum all positive day-over-day diffs | Best Time to Buy and Sell Stock II |
| "maximum jump length at each position" | Track `max_reach` waterline | Jump Game |
| "minimum arrows / groups to cover" | Sort by start, tighten window with `min()` | Minimum Arrows to Burst Balloons |

---

## Two Pointers

Use when the input is sorted or when two indices working toward each other (or one leading the other) can replace a nested loop.

| Tell | Pattern | Example |
|---|---|---|
| Merge two sorted inputs in-place | Pointers from the back, write to tail | Merge Sorted Array |
| Remove/filter in-place, return count | Forward write pointer (`index` lags `i`) | Remove Element |
| Allow at most m copies of each element | Write pointer offset by m | Remove Duplicates II |
| Sorted input + find pair/target | Left and right pointers moving inward | Two Sum II |

---

## Intervals

Use when the problem involves ranges with a start and end. Sorting by start means overlapping intervals are always adjacent — a single pass is then sufficient.

| Tell | Pattern | Example |
|---|---|---|
| Merge overlapping intervals | Sort by start, extend end with `max()` | Merge Intervals |
| Insert into sorted non-overlapping list | Three cases: before, overlap, after | Insert Interval |
| Minimum arrows / groups | Sort by start, tighten window on overlap | Minimum Arrows to Burst Balloons |

---

## Voting / Cancellation

Use when a majority constraint guarantees a survivor after pairwise elimination.

| Tell | Pattern | Example |
|---|---|---|
| "appears more than n/2 times" | Boyer-Moore Voting — reset candidate when count hits 0 | Majority Element |

---

## Modular Arithmetic

Use when a cyclic or wrapping behaviour can be expressed as a remainder.

| Tell | Pattern | Example |
|---|---|---|
| Rotate by k steps (k may exceed length) | `k = k % n` to normalise, then slice | Rotate Array |
| Index wraps around | `index % n` | Circular buffer problems |

---

*Add new patterns here as they are encountered across problem sets.*
