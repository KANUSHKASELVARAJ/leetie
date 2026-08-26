# ──────────────────────────────────────────────────
# Problem  : 2603. Collect Coins in a Tree
# Difficulty: Hard
# Tags     : Array, Tree, Graph Theory, Topological Sort
# Link     : https://leetcode.com/problems/collect-coins-in-a-tree/
# Runtime  : 278 ms (beats 25%)
# Memory   : 32576000 (beats 6%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import deque

class Solution:
    def collectTheCoins(self, coins, edges):
        n = len(coins)
        adj = [set() for _ in range(n)]
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        leaves = deque([i for i in range(n) if len(adj[i]) == 1 and coins[i] == 0])

        while leaves:
            u = leaves.popleft()
            if not adj[u]:
                continue
            v = adj[u].pop()
            adj[v].remove(u)
            if len(adj[v]) == 1 and coins[v] == 0:
                leaves.append(v)

        for _ in range(2):
            leaves = deque([i for i in range(n) if len(adj[i]) == 1])
            while leaves:
                u = leaves.popleft()
                if not adj[u]:
                    continue
                v = adj[u].pop()
                adj[v].remove(u)

        remaining_edges = 0
        for i in range(n):
            remaining_edges += len(adj[i])

        return remaining_edges