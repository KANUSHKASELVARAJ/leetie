# ──────────────────────────────────────────────────
# Problem  : 3650. Minimum Cost Path with Edge Reversals
# Difficulty: Medium
# Tags     : Graph Theory, Heap (Priority Queue), Shortest Path
# Link     : https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12356000 (beats 0%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import heapq

class Solution:
    def minCost(self, n, edges):
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w * 2))

        dist = [float('inf')] * n
        dist[0] = 0
        pq = [(0, 0)]

        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            if u == n - 1:
                return d

            for v, w in g[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))

        return -1