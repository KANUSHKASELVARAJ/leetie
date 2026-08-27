# ──────────────────────────────────────────────────
# Problem  : 77. Combinations
# Difficulty: Medium
# Tags     : Backtracking
# Link     : https://leetcode.com/problems/combinations/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12268000 (beats 0%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def combine(self, n, k):
        result = []

        def backtrack(start, current_comb):
            if len(current_comb) == k:
                result.append(current_comb[:])
                return

            # Pruning: stop if not enough elements left to reach size k
            need = k - len(current_comb)
            remain = n - start + 1
            if remain < need:
                return

            for i in range(start, n + 1):
                current_comb.append(i)
                backtrack(i + 1, current_comb)
                current_comb.pop()

        backtrack(1, [])
        return result