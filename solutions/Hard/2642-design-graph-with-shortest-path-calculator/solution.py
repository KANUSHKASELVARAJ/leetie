# ──────────────────────────────────────────────────
# Problem  : 2642. Design Graph With Shortest Path Calculator
# Difficulty: Hard
# Tags     : Graph Theory, Design, Heap (Priority Queue), Shortest Path
# Link     : https://leetcode.com/problems/design-graph-with-shortest-path-calculator/
# Runtime  : 323 ms (beats 48%)
# Memory   : 16292000 (beats 62%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import heapq

class Graph:

    def __init__(self, n, edges):
        self.n = n
        self.adj = [[] for _ in range(n)]
        for u, v, w in edges:
            self.adj[u].append((v, w))

    def addEdge(self, edge):
        u, v, w = edge
        self.adj[u].append((v, w))

    def shortestPath(self, node1, node2):
        dist = [float('inf')] * self.n
        dist[node1] = 0
        pq = [(0, node1)]

        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue

            if u == node2:
                return d

            for v, w in self.adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))

        return -1