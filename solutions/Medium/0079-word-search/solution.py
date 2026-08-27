# ──────────────────────────────────────────────────
# Problem  : 79. Word Search
# Difficulty: Medium
# Tags     : Array, String, Backtracking, Depth-First Search, Matrix
# Link     : https://leetcode.com/problems/word-search/
# Runtime  : 5774 ms (beats 64%)
# Memory   : 12352000 (beats 58%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def exist(self, board, word):
        m, n = len(board), len(board[0])

        def dfs(r, c, k):
            if k == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[k]:
                return False

            # Mark cell as visited
            temp = board[r][c]
            board[r][c] = "#"

            # Explore 4 directions
            found = (
                dfs(r + 1, c, k + 1) or
                dfs(r - 1, c, k + 1) or
                dfs(r, c + 1, k + 1) or
                dfs(r, c - 1, k + 1)
            )

            # Backtrack to restore original character
            board[r][c] = temp
            return found

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True

        return False