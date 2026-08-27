# ──────────────────────────────────────────────────
# Problem  : 56. Merge Intervals
# Difficulty: Medium
# Tags     : Array, Sorting, Quicksort
# Link     : https://leetcode.com/problems/merge-intervals/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12336000 (beats 0%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged