# ──────────────────────────────────────────────────
# Problem  : 310. Minimum Height Trees
# Difficulty: Medium
# Tags     : Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort
# Link     : https://leetcode.com/problems/minimum-height-trees/
# Runtime  : 57 ms (beats 95%)
# Memory   : 23512000 (beats 23%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import deque

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 2:
            return [i for i in range(n)]

        adj = [set() for _ in range(n)]
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        leaves = deque([i for i in range(n) if len(adj[i]) == 1])

        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count

            for _ in range(leaves_count):
                leaf = leaves.popleft()
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)

                if len(adj[neighbor]) == 1:
                    leaves.append(neighbor)

        return list(leaves)