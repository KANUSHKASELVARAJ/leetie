# ──────────────────────────────────────────────────
# Problem  : 3970. Shortest Path With At Most K Consecutive Identical Characters
# Difficulty: Medium
# Tags     : String, Graph Theory, Heap (Priority Queue), Shortest Path
# Link     : https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12340000 (beats 0%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import heapq

class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :type k: int
        :rtype: int
        """
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        
        pq = [(0, 0, 1)]
        
        while pq:
            cost, u, cnt = heapq.heappop(pq)
            
            if cost > dist[u][cnt]:
                continue
                
            if u == n - 1:
                return cost
                
            for v, w in graph[u]:
                next_cnt = cnt + 1 if labels[u] == labels[v] else 1
                
                if next_cnt <= k and cost + w < dist[v][next_cnt]:
                    dist[v][next_cnt] = cost + w
                    heapq.heappush(pq, (cost + w, v, next_cnt))
                    
        return -1