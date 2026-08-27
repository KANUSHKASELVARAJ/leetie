# ──────────────────────────────────────────────────
# Problem  : 80. Remove Duplicates from Sorted Array II
# Difficulty: Medium
# Tags     : Array, Two Pointers
# Link     : https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Runtime  : 64 ms (beats 87%)
# Memory   : 15232000 (beats 68%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def removeDuplicates(self, nums):
        k = 0
        for x in nums:
            if k < 2 or x != nums[k - 2]:
                nums[k] = x
                k += 1
        return k