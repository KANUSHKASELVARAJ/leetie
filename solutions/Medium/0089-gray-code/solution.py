# ──────────────────────────────────────────────────
# Problem  : 89. Gray Code
# Difficulty: Medium
# Tags     : Math, Backtracking, Bit Manipulation
# Link     : https://leetcode.com/problems/gray-code/
# Runtime  : 10 ms (beats 48%)
# Memory   : 20484000 (beats 80%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def grayCode(self, n):
        return [i ^ (i >> 1) for i in range(1 << n)]