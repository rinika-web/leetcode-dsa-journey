"""
LeetCode 212 - Word Search II

Pattern:
Trie + DFS + Backtracking

Difficulty:
Hard

Key Idea:
Use Trie to store words and prune invalid paths early.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.word = None
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True
        node.word = word
    

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        rows = len(board)
        cols = len(board[0])
        directions = [(0,1), (0,-1),(1,0),(-1,0)]
        visited = set()
        result = []
        def dfs(row, col, node):
            
            if (
                row<0 or row>=rows or
                col<0 or col>=cols or
                (row,col) in visited
            ):
                return 
            ch = board[row][col]
            if ch not in node.children:
                return 
            node = node.children[ch]
            if node.isEnd:
                result.append(node.word)
                node.isEnd = False
            visited.add((row,col))

            for dr,dc in directions:
                dfs(row+dr, col+dc, node)
            visited.remove((row, col))
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie.root)
        return result


if __name__ == "__main__":

    board = [
        ["o","a","a","n"],
        ["e","t","a","e"],
        ["i","h","k","r"],
        ["i","f","l","v"]
    ]

    words = ["oath","pea","eat","rain"]

    solution = Solution()

    print(solution.findWords(board, words))