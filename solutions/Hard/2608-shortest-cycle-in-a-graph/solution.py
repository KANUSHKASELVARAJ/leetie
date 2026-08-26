# ──────────────────────────────────────────────────
# Problem  : 2608. Shortest Cycle in a Graph
# Difficulty: Hard
# Tags     : Breadth-First Search, Graph Theory
# Link     : https://leetcode.com/problems/shortest-cycle-in-a-graph/
# Runtime  : 2048 ms (beats 94%)
# Memory   : 12536000 (beats 94%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import deque

class Solution:
    def findShortestCycle(self, n, edges):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        ans = float('inf')

        for i in range(n):
            dist = [-1] * n
            dist[i] = 0
            q = deque([(i, -1)])

            while q:
                u, p = q.popleft()

                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append((v, u))
                    elif v != p:
                        ans = min(ans, dist[u] + dist[v] + 1)

        return ans if ans != float('inf') else -1