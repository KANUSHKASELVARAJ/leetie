# ──────────────────────────────────────────────────
# Problem  : 3604. Minimum Time to Reach Destination in Directed Graph
# Difficulty: Medium
# Tags     : Graph Theory, Heap (Priority Queue), Shortest Path
# Link     : https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/
# Runtime  : 221 ms (beats 54%)
# Memory   : 54784000 (beats 92%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import heapq

class Solution:
    def minTime(self, n, edges):
        graph = [[] for _ in range(n)]
        for u, v, start, end in edges:
            graph[u].append((v, start, end))

        dist = [float('inf')] * n
        dist[0] = 0
        pq = [(0, 0)]

        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            if u == n - 1:
                return d

            for v, start, end in graph[u]:
                if d <= end:
                    depart_time = max(d, start)
                    arr_time = depart_time + 1
                    if arr_time < dist[v]:
                        dist[v] = arr_time
                        heapq.heappush(pq, (arr_time, v))

        return -1