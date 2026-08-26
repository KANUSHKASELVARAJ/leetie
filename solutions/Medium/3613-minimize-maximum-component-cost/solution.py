# ──────────────────────────────────────────────────
# Problem  : 3613. Minimize Maximum Component Cost
# Difficulty: Medium
# Tags     : Binary Search, Union-Find, Graph Theory, Sorting
# Link     : https://leetcode.com/problems/minimize-maximum-component-cost/
# Runtime  : 239 ms (beats 100%)
# Memory   : 49804000 (beats 38%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def minCost(self, n, edges, k):
        if k == n:
            return 0

        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        edges.sort(key=lambda x: x[2])
        components = n

        for u, v, w in edges:
            root_u, root_v = find(u), find(v)
            if root_u != root_v:
                parent[root_u] = root_v
                components -= 1
                if components <= k:
                    return w

        return 0