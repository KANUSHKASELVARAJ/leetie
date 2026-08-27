# ──────────────────────────────────────────────────
# Problem  : 55. Jump Game
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Greedy
# Link     : https://leetcode.com/problems/jump-game/
# Runtime  : 30 ms (beats 70%)
# Memory   : 13100000 (beats 98%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def canJump(self, nums):
        max_reach = 0
        for i, jump in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + jump)
            if max_reach >= len(nums) - 1:
                return True
        return True