# ──────────────────────────────────────────────────
# Problem  : 3419. Minimize the Maximum Edge Weight of Graph
# Difficulty: Medium
# Tags     : Binary Search, Depth-First Search, Breadth-First Search, Graph Theory, Shortest Path
# Link     : https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/
# Runtime  : 837 ms (beats 100%)
# Memory   : 66564000 (beats 9%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def minMaxWeight(self, n, edges, threshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[v].append((u, w))

        # Dijkstra from node 0 to find min bottleneck path cost to all other nodes
        dist = [float('inf')] * n
        dist[0] = 0
        pq = [(0, 0)]  # (bottleneck_weight, node)

        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                new_dist = max(d, w)
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))

        # If any node is unreachable from node 0 in reversed graph, return -1
        max_weight = max(dist)
        return max_weight if max_weight != float('inf') else -1
        