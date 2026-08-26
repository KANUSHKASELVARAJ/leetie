# ──────────────────────────────────────────────────
# Problem  : 3532. Path Existence Queries in a Graph I
# Difficulty: Medium
# Tags     : Array, Hash Table, Binary Search, Union-Find, Graph Theory
# Link     : https://leetcode.com/problems/path-existence-queries-in-a-graph-i/
# Runtime  : 95 ms (beats 91%)
# Memory   : 45196000 (beats 85%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        comp = [0] * n
        group_id = 0
        
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                group_id += 1
            comp[i] = group_id
            
        return [comp[u] == comp[v] for u, v in queries]
        