# ──────────────────────────────────────────────────
# Problem  : 3241. Time Taken to Mark All Nodes
# Difficulty: Hard
# Tags     : Dynamic Programming, Tree, Depth-First Search, Graph Theory, DP on Trees
# Link     : https://leetcode.com/problems/time-taken-to-mark-all-nodes/
# Runtime  : 1211 ms (beats 67%)
# Memory   : 170752000 (beats 33%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def timeTaken(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # d1[u]: max time in u's subtree (odd step = 1, even step = 2)
        # d2[u]: 2nd max time in u's subtree
        # best_child[u]: child of u that yields d1[u]
        d1 = [0] * n
        d2 = [0] * n
        best_child = [-1] * n

        # DFS 1: Bottom-up DP to compute subtree distances
        def dfs1(u, p):
            for v in adj[u]:
                if v == p:
                    continue
                dfs1(v, u)
                weight = 1 if v % 2 == 1 else 2
                val = d1[v] + weight

                if val > d1[u]:
                    d2[u] = d1[u]
                    d1[u] = val
                    best_child[u] = v
                elif val > d2[u]:
                    d2[u] = val

        dfs1(0, -1)

        ans = [0] * n

        # DFS 2: Top-down DP (re-rooting) to incorporate parent paths
        def dfs2(u, p, up_dist):
            ans[u] = max(d1[u], up_dist)

            for v in adj[u]:
                if v == p:
                    continue

                # Distance going through node u to parent/other branches
                weight_u = 1 if u % 2 == 1 else 2
                in_subtree_max = d2[u] if v == best_child[u] else d1[u]
                
                next_up = max(up_dist, in_subtree_max) + weight_u
                dfs2(v, u, next_up)

        dfs2(0, -1, 0)
        return ans
        