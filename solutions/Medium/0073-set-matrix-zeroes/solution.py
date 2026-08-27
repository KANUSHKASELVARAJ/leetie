# ──────────────────────────────────────────────────
# Problem  : 73. Set Matrix Zeroes
# Difficulty: Medium
# Tags     : Array, Hash Table, Matrix
# Link     : https://leetcode.com/problems/set-matrix-zeroes/
# Runtime  : 15 ms (beats 34%)
# Memory   : 13740000 (beats 37%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = any(matrix[0][c] == 0 for c in range(n))
        first_col_has_zero = any(matrix[r][0] == 0 for r in range(m))

        # Use first row and column as markers
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Zero out cells based on markers
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Zero out the first row if needed
        if first_row_has_zero:
            for c in range(n):
                matrix[0][c] = 0

        # Zero out the first column if needed
        if first_col_has_zero:
            for r in range(m):
                matrix[r][0] = 0