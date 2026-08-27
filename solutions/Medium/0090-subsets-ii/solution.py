# ──────────────────────────────────────────────────
# Problem  : 90. Subsets II
# Difficulty: Medium
# Tags     : Array, Backtracking, Bit Manipulation
# Link     : https://leetcode.com/problems/subsets-ii/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12680000 (beats 42%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        result = []

        def backtrack(start, current_subset):
            result.append(current_subset[:])

            for i in range(start, len(nums)):
                # Skip duplicate elements at the same recursion depth
                if i > start and nums[i] == nums[i - 1]:
                    continue

                current_subset.append(nums[i])
                backtrack(i + 1, current_subset)
                current_subset.pop()

        backtrack(0, [])
        return result