# ──────────────────────────────────────────────────
# Problem  : 2699. Modify Graph Edge Weights
# Difficulty: Hard
# Tags     : Graph Theory, Heap (Priority Queue), Shortest Path
# Link     : https://leetcode.com/problems/modify-graph-edge-weights/
# Runtime  : 1997 ms (beats 55%)
# Memory   : 16080000 (beats 18%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import heapq

class Solution:
    def modifiedGraphEdges(self, n, edges, source, destination, target):
        adj = [[] for _ in range(n)]
        for i, (u, v, w) in enumerate(edges):
            if w != -1:
                adj[u].append((v, w))
                adj[v].append((u, w))

        def dijkstra():
            dist = [float('inf')] * n
            dist[source] = 0
            pq = [(0, source)]
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]:
                    continue
                for v, w in adj[u]:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        heapq.heappush(pq, (dist[v], v))
            return dist[destination]

        current_dist = dijkstra()
        if current_dist < target:
            return []

        if current_dist == target:
            for i in range(len(edges)):
                if edges[i][2] == -1:
                    edges[i][2] = 2 * 10**9
            return edges

        for i, (u, v, w) in enumerate(edges):
            if w != -1:
                continue

            edges[i][2] = 1
            adj[u].append((v, 1))
            adj[v].append((u, 1))

            new_dist = dijkstra()

            if new_dist <= target:
                edges[i][2] += target - new_dist
                for j in range(i + 1, len(edges)):
                    if edges[j][2] == -1:
                        edges[j][2] = 2 * 10**9
                return edges

        return []