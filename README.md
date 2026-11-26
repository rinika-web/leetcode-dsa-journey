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
| Arrays | 3 |
| Strings | 1 |
| Linked List | Coming Soon |
| Stack & Queue | Coming Soon |
| Binary Search | Coming Soon |
| Trees | Coming Soon |
| Graphs | 2 |
| Dynamic Programming | 1 |
| Backtracking | 1 |
| Trie | 1 |
| Two Pointers | 2 |
| Sliding Window | 1 |
| Prefix/Suffix Products | 1 |
| Greedy | Coming Soon |

---

# 🧠 Problem Patterns

## Two Pointers

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 11 | Container With Most Water | Medium | Two Pointers |
| 42 | Trapping Rain Water | Hard | Two Pointers + Left/Right Maximums |

---

## Sliding Window

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 424 | Longest Repeating Character Replacement | Medium | Sliding Window + Hash Map |

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

## Dynamic Programming

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 198 | House Robber | Medium | Dynamic Programming + Space Optimization |

---
## Graph Theory / Topological Sort

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 2115 | Find All Possible Recipes from Given Supplies | Medium | Topological Sort + BFS |
| 207 | Course Schedule | Medium | Topological Sort + BFS (Kahn's Algorithm) |

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

## LeetCode 42 - Trapping Rain Water

### Concepts:

- Two Pointers
- Left Maximum
- Right Maximum
- Array Traversal
- Space Optimization

### Key Learning:

The amount of water that can be trapped at a position depends on the maximum height of the bars on both sides.

A straightforward approach can precompute the left and right maximum heights, but that requires **O(n)** extra space.

The optimized two-pointer approach maintains:

- `left_max` → maximum height seen from the left
- `right_max` → maximum height seen from the right

At each step, process the side with the **smaller current height**, because that side determines the limiting water level.

If the current height is below the maximum boundary on that side, water can be trapped:

```text
water += max_height - current_height
```

This allows the problem to be solved in a single traversal without storing additional arrays.

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

## LeetCode 198 - House Robber

### Concepts:

- Dynamic Programming
- Bottom-Up DP
- Recurrence Relation
- Space Optimization

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

- `next1` → maximum amount from the next house onward
- `next2` → maximum amount from two houses ahead

For each house:

```text
current = max(nums[i] + next2, next1)
```

Then the DP states are shifted forward.

### Complexity:

- Time: **O(n)**
- Space: **O(1)**

---

## LeetCode 424 - Longest Repeating Character Replacement

### Concepts:

- Sliding Window
- Hash Map
- Character Frequency
- Window Validation
- Space Optimization

### Key Learning:

The goal is to find the longest substring that can be converted into a string containing the same character using at most `k` replacements.

The key observation is:

```text
Window Length - Maximum Character Frequency <= k
```

The difference between the window length and the highest character frequency represents the minimum number of replacements needed to make all characters in the current window identical.

The solution uses:

- `count` → tracks the frequency of each character
- `left` → left boundary of the sliding window
- `right` → right boundary of the sliding window
- `max_freq` → maximum character frequency observed
- `max_length` → longest valid window found

Whenever the number of required replacements exceeds `k`, shrink the window from the left.

Once the window is valid, update the maximum length.

The solution uses a constant-size character frequency map because the input contains only uppercase English letters.

### Complexity:

- Time: **O(n)**
- Space: **O(1)**

---

---

## LeetCode 2115 - Find All Possible Recipes from Given Supplies

**### Concepts:**

- Graph Theory
- Topological Sorting
- Breadth-First Search (BFS)
- Dependency Resolution
- Indegree

**### Key Learning:**

This problem can be modeled as a dependency graph where each recipe depends on a list of ingredients.

The key idea is to process available ingredients and use them to unlock recipes whose dependencies have been satisfied.

Using Topological Sort with BFS:

1. Build a graph connecting each ingredient to the recipes that require it.
2. Calculate the indegree of each recipe, representing the number of ingredients it still needs.
3. Initialize the BFS queue with all available supplies.
4. Process each available ingredient and reduce the indegree of the recipes that depend on it.
5. When a recipe's indegree becomes zero, all its required ingredients are available, so the recipe can be added to the queue.

A newly available recipe can also act as an ingredient for other recipes, allowing the process to continue.

**### Complexity:**

- Time: **O(R + I + E)**
- Space: **O(R + I + E)**

Where:
- `R` = Number of recipes
- `I` = Number of distinct ingredients and supplies
- `E` = Total number of ingredient dependencies

---

## LeetCode 207 - Course Schedule

**### Concepts:**

- Graph Theory
- Directed Graph
- Topological Sorting
- Breadth-First Search (BFS)
- Kahn's Algorithm
- Cycle Detection
- Indegree

**### Key Learning:**

The problem asks whether all courses can be completed when some courses have prerequisite dependencies.

The solution uses Topological Sorting with BFS (Kahn's Algorithm).

The main idea is to process courses that have no prerequisites first.

1. Build a directed graph where each prerequisite points to the course that depends on it.
2. Calculate the indegree of every course, representing the number of prerequisites it has.
3. Add all courses with an indegree of zero to the queue.
4. Process each course and decrease the indegree of its dependent courses.
5. Whenever a dependent course reaches an indegree of zero, add it to the queue.

Maintain a `process` counter to track the number of courses completed.

The final condition is:

```python
return process == numCourses

---

# 📂 Repository Structure

```text
LeetCode-DSA-Journey/
│
├── Arrays/
│   ├── 011-Container-With-Most-Water/
│   ├── 042-Trapping-Rain-Water/
│   └── 238-Product-of-Array-Except-Self/
│
├── Strings/
│   └── 424-Longest-Repeating-Character-Replacement/
│
├── Dynamic-Programming/
│   └── 198-House-Robber/
│
├── Backtracking/
│   └── 212-Word-Search-II/
├── Graphs/
│   └── 2115-Find-All-Possible-Recipes-from-Given-Supplies/
│   └── 2115-Find-All-Possible-Recipes-from-Given-Supplies/
│
└── README.md
```

---

# 📈 Progress

Currently documented problems:

- **Arrays:** 3
- **Strings:** 1
- **Dynamic Programming:** 1
- **Backtracking:** 1
- **Graphs:** 1
- **Trie:** 1
- **Two Pointers:** 2
- **Sliding Window:** 1
- **Prefix/Suffix Products:** 1

**Total: 7 problems**

---

# 🧩 Patterns I'm Learning

The goal is not just to solve individual problems, but to recognize reusable patterns.

Current patterns include:

- Two Pointers
- Sliding Window
- Prefix / Suffix Products
- Trie + DFS + Backtracking
- Dynamic Programming
- Space Optimization
- Graph Theory
- Topological Sorting + BFS

As the repository grows, more patterns will be added, including:

- Hash Maps
- Binary Search
- Stack / Monotonic Stack
- Linked Lists
- Trees
- Greedy
- Backtracking

---

# 🚀 Why This Repository?

I'm using this repository to document my progress in **Data Structures & Algorithms** and strengthen the problem-solving skills required for Software Engineering interviews.

For each problem, I focus on:

**Understanding → Pattern Recognition → Optimization → Implementation → Complexity Analysis**

The goal is to understand **why a solution works**, not simply memorize it.