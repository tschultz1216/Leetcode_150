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
│   └── majority_element.py
└── .bob/
    └── agents.md          # Pattern library and project instructions for Bob
```

## Patterns Covered So Far

| Pattern | Problems |
|---|---|
| Two pointers — fill from back | Merge Sorted Array |
| Forward write pointer | Remove Element, Remove Duplicates I & II |
| Write pointer offset by m | Remove Duplicates II |
| Boyer-Moore Voting | Majority Element |

## Running a Problem

Each file is self-contained and runnable:

```bash
python3 arrays/majority_element.py
```

Test output uses `✅` / `❌` to show pass/fail alongside the actual and expected values.

## Requirements

- Python 3
- No external dependencies
