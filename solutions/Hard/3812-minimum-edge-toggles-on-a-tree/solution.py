# ──────────────────────────────────────────────────
# Problem  : 3812. Minimum Edge Toggles on a Tree
# Difficulty: Hard
# Tags     : Tree, Depth-First Search, Graph Theory, Topological Sort, Sorting
# Link     : https://leetcode.com/problems/minimum-edge-toggles-on-a-tree/
# Runtime  : 1042 ms (beats 33%)
# Memory   : 177332000 (beats 17%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import sys


sys.setrecursionlimit(200000)

class Solution:
    def minimumFlips(self, n, edges, start, target):
        graph = [[] for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, i))
            graph[v].append((u, i))

        ans = []

        def dfs(u, parent):
            need_flip = start[u] != target[u]
            for v, idx in graph[u]:
                if v != parent:
                    if dfs(v, u):
                        ans.append(idx)
                        need_flip = not need_flip
            return need_flip

        if dfs(0, -1):
            return [-1]

        ans.sort()
        return ans