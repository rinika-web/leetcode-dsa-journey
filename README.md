# 🚀 LeetCode DSA Journey

A collection of my solutions, notes, and learnings while mastering **Data Structures & Algorithms** for Software Engineering interviews.

This repository documents my problem-solving journey through different algorithmic patterns, focusing on understanding **why a solution works**, not just writing code.

---

## 🎯 Goals

* Strengthen Data Structures & Algorithms fundamentals
* Master common coding interview patterns
* Improve problem-solving and optimization skills
* Prepare for Software Engineering interviews

---

# 📚 Topics Covered

| Topic                  | Problems    |
| ---------------------- | ----------- |
| Arrays                 | 3           |
| Strings                | Coming Soon |
| Linked List            | Coming Soon |
| Stack & Queue          | Coming Soon |
| Binary Search          | Coming Soon |
| Trees                  | Coming Soon |
| Graphs                 | Coming Soon |
| Dynamic Programming    | 1           |
| Backtracking           | 1           |
| Trie                   | 1           |
| Two Pointers           | 2           |
| Prefix/Suffix Products | 1           |
| Greedy                 | Coming Soon |

---

# 🧠 Problem Patterns

## Two Pointers

| #  | Problem                   | Difficulty | Approach                           |
| -- | ------------------------- | ---------- | ---------------------------------- |
| 11 | Container With Most Water | Medium     | Two Pointers                       |
| 42 | Trapping Rain Water       | Hard       | Two Pointers + Left/Right Maximums |

---

## Prefix / Suffix Products

| #   | Problem                      | Difficulty | Approach                        |
| --- | ---------------------------- | ---------- | ------------------------------- |
| 238 | Product of Array Except Self | Medium     | Prefix Product + Suffix Product |

---

## Trie

| #   | Problem        | Difficulty | Approach                  |
| --- | -------------- | ---------- | ------------------------- |
| 212 | Word Search II | Hard       | Trie + DFS + Backtracking |

---

## Dynamic Programming

| #   | Problem      | Difficulty | Approach                                 |
| --- | ------------ | ---------- | ---------------------------------------- |
| 198 | House Robber | Medium     | Dynamic Programming + Space Optimization |

---

# 🔥 Featured Problems

## LeetCode 11 - Container With Most Water

### Concepts:

* Two Pointers
* Greedy Decision
* Array Traversal
* Space Optimization

### Key Learning:

Instead of checking every possible pair of lines with an **O(n²)** brute-force approach, two pointers allow us to start with the widest container and eliminate impossible pairs.

At every step, move the pointer with the **smaller height**, because the smaller height is limiting the current container.

### Complexity:

* Time: **O(n)**
* Space: **O(1)**

---

## LeetCode 42 - Trapping Rain Water

### Concepts:

* Two Pointers
* Left Maximum
* Right Maximum
* Array Traversal
* Space Optimization

### Key Learning:

The amount of water that can be trapped at a position depends on the maximum height of the bars on both sides.

A straightforward approach can precompute the left and right maximum heights, but that requires **O(n)** extra space.

The optimized two-pointer approach maintains:

* `left_max` → maximum height seen from the left
* `right_max` → maximum height seen from the right

At each step, compare the heights at the two pointers.

The side with the **smaller current height** can be processed because that side determines the limiting water level.

If the current height is below the maximum boundary on that side, water can be trapped:

```text
water += max_height - current_height
```

This allows the problem to be solved in a single traversal without storing additional arrays.

### Complexity:

* Time: **O(n)**
* Space: **O(1)**

---

## LeetCode 212 - Word Search II

### Concepts:

* Trie (Prefix Tree)
* DFS Traversal
* Backtracking
* Prefix Pruning

### Key Learning:

Instead of searching every word separately, a Trie allows multiple words to share prefixes and helps eliminate unnecessary searches during DFS traversal.

### Complexity:

* Trie: **O(total characters in all words)**
* DFS + Backtracking: Depends on board size and maximum word length

---

## LeetCode 238 - Product of Array Except Self

### Concepts:

* Prefix Product
* Suffix Product
* Array Traversal
* Space Optimization

### Key Learning:

Instead of using division or calculating the product repeatedly, calculate the product of all elements **to the left** of each index and then multiply it by the product of all elements **to the right**.

The solution uses two passes:

1. Left-to-right → store prefix products
2. Right-to-left → multiply suffix products

### Complexity:

* Time: **O(n)**
* Space: **O(1)** extra space, excluding the output array

---

## LeetCode 198 - House Robber

### Concepts:

* Dynamic Programming
* Bottom-Up DP
* Recurrence Relation
* Space Optimization

### Key Learning:

At every house, there are two choices:

1. **Rob the current house** → add its money to the maximum amount from two houses ahead.
2. **Skip the current house** → keep the maximum amount calculated for the next house.

The recurrence is:

```text
dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
```

Instead of storing the entire DP array, only the results for the **next two positions** are needed.

The solution processes the houses from **right to left** using two variables:

* `next1` → maximum amount from the next house onward
* `next2` → maximum amount from two houses ahead

For each house:

```text
current = max(nums[i] + next2, next1)
```

Then the DP states are shifted forward.

### Complexity:

* Time: **O(n)**
* Space: **O(1)**

---

# 📈 Progress

Currently solved problems:

* **Arrays:** 3
* **Dynamic Programming:** 1
* **Backtracking:** 1
* **Trie:** 1
* **Two Pointers:** 2
* **Prefix/Suffix Products:** 1

**Total: 5 problems**

---

# 🧩 Patterns I'm Learning

The goal is not just to solve individual problems, but to recognize reusable patterns.

Current patterns include:

* Two Pointers
* Prefix / Suffix Products
* Trie + DFS + Backtracking
* Dynamic Programming
* Space Optimization

As the repository grows, more patterns will be added, including:

* Hash Maps
* Sliding Window
* Binary Search
* Stack / Monotonic Stack
* Linked Lists
* Trees
* Graphs
* Greedy
* Dynamic Programming
* Backtracking

---

# 🚀 Why This Repository?

I'm using this repository to document my progress in **Data Structures & Algorithms** and strengthen the problem-solving skills required for Software Engineering interviews.

For each problem, I focus on:

**Understanding → Pattern Recognition → Optimization → Implementation → Complexity Analysis**

The goal is to understand **why a solution works**, not simply memorize it.
