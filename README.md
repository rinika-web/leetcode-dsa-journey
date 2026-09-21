# 🚀 LeetCode DSA Journey

A collection of my solutions, notes, and learnings while mastering **Data Structures & Algorithms** for Software Engineering interviews.

This repository documents my problem-solving journey through different algorithmic patterns, focusing on understanding **why a solution works**, not just writing code.

---

## 🎯 Goals

- Strengthen Data Structures & Algorithms fundamentals
- Master common coding interview patterns
- Improve problem-solving and optimization skills
- Prepare for Software Engineering interviews

---

# 📚 Topics Covered

| Topic | Problems |
|------|----------|
| Arrays | 2 |
| Strings | Coming Soon |
| Linked List | Coming Soon |
| Stack & Queue | Coming Soon |
| Binary Search | Coming Soon |
| Trees | Coming Soon |
| Graphs | Coming Soon |
| Dynamic Programming | Coming Soon |
| Backtracking | 1 |
| Trie | 1 |
| Two Pointers | 1 |
| Prefix/Suffix | 1 |
| Greedy | Coming Soon |

---

# 🧠 Problem Patterns

## Two Pointers

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 11 | Container With Most Water | Medium | Two Pointers |

---

## Prefix / Suffix Products

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 238 | Product of Array Except Self | Medium | Prefix Product + Suffix Product |

---

## Trie

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 212 | Word Search II | Hard | Trie + DFS + Backtracking |

---

# 🔥 Featured Problems

## LeetCode 11 - Container With Most Water

### Concepts:

- Two Pointers
- Greedy Decision
- Array Traversal
- Space Optimization

### Key Learning:

Instead of checking every possible pair of lines with an **O(n²)** brute-force approach, two pointers allow us to start with the widest container and eliminate impossible pairs.

At every step, move the pointer with the **smaller height**, because the smaller height is limiting the current container.

### Complexity:

- Time: **O(n)**
- Space: **O(1)**

---

## LeetCode 212 - Word Search II

### Concepts:

- Trie (Prefix Tree)
- DFS Traversal
- Backtracking
- Prefix Pruning

### Key Learning:

Instead of searching every word separately, a Trie allows multiple words to share prefixes and helps eliminate unnecessary searches during DFS traversal.

### Complexity:

- Trie: **O(total characters in all words)**
- DFS + Backtracking: Depends on board size and maximum word length

---

## LeetCode 238 - Product of Array Except Self

### Concepts:

- Prefix Product
- Suffix Product
- Array Traversal
- Space Optimization

### Key Learning:

Instead of using division or calculating the product repeatedly, calculate the product of all elements **to the left** of each index and then multiply it by the product of all elements **to the right**.

The solution uses two passes:

1. Left-to-right → store prefix products
2. Right-to-left → multiply suffix products

### Complexity:

- Time: **O(n)**
- Space: **O(1)** extra space, excluding the output array

---

