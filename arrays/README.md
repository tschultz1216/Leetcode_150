# Arrays

LeetCode array problems practiced with solutions and explanations.

## Problems

### [Merge Sorted Array](./merge_sorted_array.py)
**LeetCode 88** — Merge two sorted arrays `nums1` and `nums2` into `nums1` in-place, where `nums1` has enough trailing zeros to hold both.

- **Pattern:** Two pointers — fill from the back
- **Complexity:** O(m + n) time, O(1) space

---

### [Remove Element](./remove_element.py)
**LeetCode 27** — Remove all occurrences of `val` from `nums` in-place and return the count of remaining elements.

- **Pattern:** Forward write pointer
- **Complexity:** O(n) time, O(1) space

---

### [Remove Duplicates from Sorted Array](./remove_duplicates.py)
**LeetCode 26** — Remove duplicates from a sorted array in-place so each element appears once. Return the count of unique elements.

- **Pattern:** Forward write pointer — compare against `nums[index - 1]`
- **Complexity:** O(n) time, O(1) space

---

### [Remove Duplicates from Sorted Array II](./remove_duplicates_ii.py)
**LeetCode 80** — Remove duplicates from a sorted array in-place so each element appears at most twice. Return the count.

- **Pattern:** Write pointer offset by m — compare against `nums[index - 2]`
- **Complexity:** O(n) time, O(1) space

---

### [Majority Element](./majority_element.py)
**LeetCode 169** — Find the element that appears more than `n // 2` times. It is guaranteed to always exist.

- **Pattern:** Boyer-Moore Voting Algorithm
- **Complexity:** O(n) time, O(1) space

---

### [Rotate Array](./rotate_array.py)
**LeetCode 189** — Rotate an array to the right by `k` steps in-place.

- **Pattern:** Slice reassignment with `k % n` normalisation
- **Complexity:** O(n) time, O(n) aux space

---

### [Best Time to Buy and Sell Stock](./best_time_to_buy_sell_stock.py)
**LeetCode 121** — Find the maximum profit from a single buy/sell transaction where buy must come before sell.

- **Pattern:** Track running minimum price + maximum profit
- **Complexity:** O(n) time, O(1) space

---

### [Best Time to Buy and Sell Stock II](./best_time_to_buy_sell_stock_ii.py)
**LeetCode 122** — Find the maximum profit with unlimited buy/sell transactions (at most one share held at a time).

- **Pattern:** Sum all positive day-over-day price differences
- **Complexity:** O(n) time, O(1) space

---

### [Jump Game](./jump_game.py)
**LeetCode 55** — Given jump lengths at each index, return whether you can reach the last index from index 0.

- **Pattern:** Greedy reachability — track `max_reach` waterline
- **Complexity:** O(n) time, O(1) space

---

### [Jump Game II](./jump_game_ii.py)
**LeetCode 45** — Given jump lengths at each index, return the minimum number of jumps to reach the last index.

- **Pattern:** Greedy level expansion — track `farthest` and `current_end` boundary
- **Complexity:** O(n) time, O(1) space

---

### [H-Index](./h_index.py)
**LeetCode 274** — Given citation counts, return the maximum h such that at least h papers have at least h citations each.

- **Pattern:** Sort descending, walk until `citations[i] < i + 1`
- **Complexity:** O(n log n) time, O(1) space. O(n) time possible with counting sort (bucket by citation count capped at n)

---

### [Insert Delete GetRandom O(1)](./randomized_set.py)
**LeetCode 380** — Implement a set with O(1) insert, remove, and getRandom (uniform probability).

- **Pattern:** List + HashMap — list for O(1) random access, map for O(1) index lookup; swap-and-pop for O(1) removal
- **Complexity:** O(1) average time per operation, O(n) space

---

### [Product of Array Except Self](./product_except_self.py)
**LeetCode 238** — Return an array where each element is the product of all other elements. O(n) time, no division.

- **Pattern:** Prefix and suffix product arrays — two passes, combine with multiplication
- **Complexity:** O(n) time, O(n) space

---

### [Gas Station](./gas_station.py)
**LeetCode 134** — Find the starting gas station index to complete a circular route, or return -1 if impossible.

- **Pattern:** Greedy — track running tank; when tank goes negative, reset start to next station; validate with total gas check
- **Complexity:** O(n) time, O(1) space

---

## Core Patterns

| Tell | Pattern | Key Operation |
|---|---|---|
| Merge two sorted inputs in-place | Two pointers from the back | Compare from tail, write to tail |
| Remove/filter in-place, return count | Forward write pointer | `nums[index] = nums[i]` when condition met |
| Allow at most m copies | Write pointer offset by m | Compare `nums[i] != nums[index - m]` |
| "appears more than n/2 times" | Boyer-Moore Voting | Reset candidate when count hits 0 |
| Rotate by k steps | Slice reassignment + modulo | `nums[:] = nums[n-k:] + nums[:n-k]` |
| Single buy/sell transaction | Running minimum + max profit | `profit = max(profit, price - min_price)` |
| Unlimited buy/sell transactions | Sum positive consecutive diffs | `profit += prices[i] - prices[i-1]` if positive |
| Yes/no reachability, max jump lengths | Greedy waterline | `max_reach = max(max_reach, i + nums[i])` |
| Minimum jumps, max jump lengths | Greedy level expansion | Increment jumps when `i == current_end`, set `current_end = farthest` |
| Maximum h where h papers have ≥ h citations | Sort descending, walk until rank exceeds count | `citations[i] < i + 1` → return `i` |
| O(1) insert/remove/random on a set | List + HashMap with swap-and-pop | Map stores index; swap removed element with last, pop tail, update map |
| Product of all elements except self, no division | Prefix × suffix product arrays | Two passes: left running product, right running product, multiply together |
| Circular route — find valid start or -1 | Greedy candidate reset | Reset start when tank < 0; valid only if `sum(gas) >= sum(cost)` |

