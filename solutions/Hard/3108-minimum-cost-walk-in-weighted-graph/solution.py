# ──────────────────────────────────────────────────
# Problem  : 3108. Minimum Cost Walk in Weighted Graph
# Difficulty: Hard
# Tags     : Array, Bit Manipulation, Union-Find, Graph Theory
# Link     : https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12208000 (beats 0%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def minimumCost(self, n, edges, query):
        parent = list(range(n))

        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            root_u = find(u)
            root_v = find(v)
            if root_u != root_v:
                parent[root_v] = root_u

        # Step 1: Connect nodes into components
        for u, v, w in edges:
            union(u, v)

        # Step 2: Compute bitwise AND of all edge weights in each component
        # -1 (all bits set to 1) serves as bitwise AND identity
        component_and = [-1] * n
        for u, v, w in edges:
            root = find(u)
            component_and[root] &= w

        # Step 3: Answer queries
        res = []
        for u, v in query:
            if u == v:
                res.append(0)
            else:
                root_u = find(u)
                root_v = find(v)
                if root_u == root_v:
                    res.append(component_and[root_u])
                else:
                    res.append(-1)

        return res