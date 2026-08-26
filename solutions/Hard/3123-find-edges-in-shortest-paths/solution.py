# ──────────────────────────────────────────────────
# Problem  : 3123. Find Edges in Shortest Paths
# Difficulty: Hard
# Tags     : Depth-First Search, Breadth-First Search, Graph Theory, Heap (Priority Queue), Shortest Path
# Link     : https://leetcode.com/problems/find-edges-in-shortest-paths/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12324000 (beats 0%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findAnswer(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[bool]
        """
        adj = [[] for _ in range(n)]
        for i, (u, v, w) in enumerate(edges):
            adj[u].append((v, w, i))
            adj[v].append((u, w, i))

        def dijkstra(start):
            dist = [float('inf')] * n
            dist[start] = 0
            pq = [(0, start)]
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]:
                    continue
                for v, w, _ in adj[u]:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        heapq.heappush(pq, (dist[v], v))
            return dist

        dist_from_0 = dijkstra(0)
        dist_from_n = dijkstra(n - 1)

        shortest_path_len = dist_from_0[n - 1]
        if shortest_path_len == float('inf'):
            return [False] * len(edges)

        ans = [False] * len(edges)
        for i, (u, v, w) in enumerate(edges):
            if (dist_from_0[u] + w + dist_from_n[v] == shortest_path_len) or \
               (dist_from_0[v] + w + dist_from_n[u] == shortest_path_len):
                ans[i] = True

        return ans
        