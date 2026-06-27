# Interval Problems

LeetCode interval problems practiced with solutions and explanations.

## Problems

### [Merge Intervals](./merge_intervals.py)
**LeetCode 56** — Given an array of intervals, merge all overlapping intervals and return the minimal non-overlapping list.

- **Pattern:** Sort by start, single pass
- **Complexity:** O(n log n) time, O(n) space

---

### [Insert Interval](./insert_interval.py)
**LeetCode 57** — Given a sorted list of non-overlapping intervals and a new interval, insert it and merge any overlaps.

- **Pattern:** Single pass with three cases — before, after, overlap
- **Complexity:** O(n) time, O(n) space

---

### [Minimum Arrows to Burst Balloons](./arrows_balloons.py)
**LeetCode 452** — Given balloon intervals on an x-axis, find the minimum number of arrows needed to burst all balloons.

- **Pattern:** Sort by start, track tightest arrow window with `min()`
- **Complexity:** O(n log n) time, O(1) space

---

## Core Patterns

| Tell | Pattern | Key Operation |
|---|---|---|
| Merge overlapping intervals | Sort by start, single pass | `max()` to extend end |
| Insert into sorted intervals | Three-case if/elif/else | expand with `min`/`max`, flag for insertion |
| Minimum groups / arrows | Sort by start, count gaps | `min()` to tighten window, reset on gap |

## Key Insight

> Sorting by start value means overlapping intervals are always adjacent. You never need to look further back than the last element — making a single O(n) pass sufficient after the sort.
