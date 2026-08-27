# ──────────────────────────────────────────────────
# Problem  : 59. Spiral Matrix II
# Difficulty: Medium
# Tags     : Array, Matrix, Simulation
# Link     : https://leetcode.com/problems/spiral-matrix-ii/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12328000 (beats 0%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    # Indented 4 spaces inside the class
    def generateMatrix(self, n):
        matrix = [[0] * n for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        val = 1
        
        while left <= right and top <= bottom:
            for col in range(left, right + 1):
                matrix[top][col] = val
                val += 1
            top += 1
            
            for row in range(top, bottom + 1):
                matrix[row][right] = val
                val += 1
            right -= 1
            
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = val
                val += 1
            bottom -= 1
            
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = val
                val += 1
            left += 1
            
        return matrix