# ──────────────────────────────────────────────────
# Problem  : 78. Subsets
# Difficulty: Medium
# Tags     : Array, Backtracking, Bit Manipulation
# Link     : https://leetcode.com/problems/subsets/
# Runtime  : 1 ms (beats 19%)
# Memory   : 12616000 (beats 24%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def subsets(self, nums):
        result = []
        
        def backtrack(start, current_subset):
            # Every valid state along the path is a subset
            result.append(current_subset[:])
            
            for i in range(start, len(nums)):
                current_subset.append(nums[i])
                backtrack(i + 1, current_subset)
                current_subset.pop()
                
        backtrack(0, [])
        return result