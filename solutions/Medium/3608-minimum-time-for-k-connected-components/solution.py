# ──────────────────────────────────────────────────
# Problem  : 3608. Minimum Time for K Connected Components
# Difficulty: Medium
# Tags     : Binary Search, Union-Find, Graph Theory, Sorting
# Link     : https://leetcode.com/problems/minimum-time-for-k-connected-components/
# Runtime  : 239 ms (beats 78%)
# Memory   : 39788000 (beats 11%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def minTime(self, n, edges, k):
        parent = list(range(n))

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i, root_j = find(i), find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                return True
            return False

        # Sort edges by removal time in ascending order
        edges.sort(key=lambda x: x[2])
        
        cnt = n
        
        # Process edges backwards (from highest removal time to lowest)
        for u, v, t in reversed(edges):
            if union(u, v):
                cnt -= 1
                if cnt < k:
                    return t

        return 0