# ──────────────────────────────────────────────────
# Problem  : 2858. Minimum Edge Reversals So Every Node Is Reachable
# Difficulty: Hard
# Tags     : Dynamic Programming, Depth-First Search, Breadth-First Search, Graph Theory
# Link     : https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/
# Runtime  : 1392 ms (beats 12%)
# Memory   : 240808000 (beats 12%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import defaultdict

class Solution:
    def minEdgeReversals(self, n, edges):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append((v, 0)) 
            adj[v].append((u, 1))  

        ans = [0] * n

       
        def dfs1(u, p):
            total = 0
            for v, cost in adj[u]:
                if v != p:
                    total += cost + dfs1(v, u)
            return total

        ans[0] = dfs1(0, -1)

        
        def dfs2(u, p):
            for v, cost in adj[u]:
                if v != p:
                   
                    ans[v] = ans[u] + (1 if cost == 0 else -1)
                    dfs2(v, u)

        dfs2(0, -1)
        return ans