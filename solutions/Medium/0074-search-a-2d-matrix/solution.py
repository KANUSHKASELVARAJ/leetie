# ──────────────────────────────────────────────────
# Problem  : 74. Search a 2D Matrix
# Difficulty: Medium
# Tags     : Array, Binary Search, Matrix
# Link     : https://leetcode.com/problems/search-a-2d-matrix/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12344000 (beats 0%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
            
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            mid_val = matrix[row][col]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False