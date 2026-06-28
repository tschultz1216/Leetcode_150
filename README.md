# LeetCode 150 — Interview Prep

This project uses [IBM's Bob](https://www.ibm.com/products/bob) coding tool as an interactive test bed to build and learn the patterns needed to solve the [LeetCode Top 150 Interview Questions](https://leetcode.com/studyplan/top-interview-150/) in Python 3.

## Purpose

The goal is not just to solve problems — it is to build a reusable mental catalogue of patterns that can be recognised and applied independently, under time pressure, without AI assistance. Each problem is worked through interactively with Bob: attempting a solution, getting feedback on logic errors, understanding why an approach works or fails, and connecting it back to a named pattern.

## How It Works

- Problems are grouped by topic under their own directory (e.g. `arrays/`)
- Each file contains a single problem in LeetCode-style class structure with a runnable `__main__` test block
- Solutions are written first, then checked — Bob explains what is wrong with the logic without giving away the answer
- Once solved, time and space complexity is analysed
- Patterns and common mistakes are recorded in `.bob/agents.md` as a living pattern library

## Structure

```
.
├── arrays/
│   ├── merge_sorted_array.py
│   ├── remove_element.py
│   ├── remove_duplicates.py
│   ├── remove_duplicates_ii.py
│   ├── majority_element.py
│   ├── rotate_array.py
│   ├── best_time_to_buy_sell_stock.py
│   ├── best_time_to_buy_sell_stock_ii.py
│   └── jump_game.py
└── .bob/
    └── agents.md          # Pattern library and project instructions for Bob
```

## Patterns Covered So Far

### Arrays

| Pattern | Tell | Problems |
|---|---|---|
| Two pointers — fill from back | Merge two sorted inputs into one in-place | Merge Sorted Array |
| Forward write pointer | Remove/filter elements in-place, return count | Remove Element, Remove Duplicates I & II |
| Write pointer offset by m | Allow at most m copies of each element | Remove Duplicates II |
| Boyer-Moore Voting | "appears more than n/2 times" | Majority Element |
| Slice reassignment + modulo | Rotate array by k steps in-place | Rotate Array |
| Running minimum + max profit | "single day to buy, different day to sell" | Best Time to Buy and Sell Stock |
| Sum positive day-over-day diffs | "buy and sell multiple times" | Best Time to Buy and Sell Stock II |
| Greedy reachability (waterline) | "maximum jump length at each position" | Jump Game |

## Running a Problem

Each file is self-contained and runnable:

```bash
python3 arrays/jump_game.py
```

Test output uses `✅` / `❌` to show pass/fail alongside the actual and expected values.

## Requirements

- Python 3
- No external dependencies
