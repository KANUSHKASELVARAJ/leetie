# ──────────────────────────────────────────────────
# Problem  : 64. Minimum Path Sum
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Matrix
# Link     : https://leetcode.com/problems/minimum-path-sum/
# Runtime  : 20 ms (beats 23%)
# Memory   : 13720000 (beats 72%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        
        # Fill first row
        for c in range(1, n):
            grid[0][c] += grid[0][c - 1]
            
        # Fill first column
        for r in range(1, m):
            grid[r][0] += grid[r - 1][0]
            
        # Fill rest of the grid
        for r in range(1, m):
            for c in range(1, n):
                grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])
                
        return grid[m - 1][n - 1]