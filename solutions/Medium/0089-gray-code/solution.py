# ──────────────────────────────────────────────────
# Problem  : 89. Gray Code
# Difficulty: Medium
# Tags     : Math, Backtracking, Bit Manipulation
# Link     : https://leetcode.com/problems/gray-code/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12384000 (beats 0%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def grayCode(self, n):
        return [i ^ (i >> 1) for i in range(1 << n)]