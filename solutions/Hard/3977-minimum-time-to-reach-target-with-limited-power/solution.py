# ──────────────────────────────────────────────────
# Problem  : 3977. Minimum Time to Reach Target With Limited Power
# Difficulty: Hard
# Tags     : Array, Dynamic Programming, Graph Theory, Heap (Priority Queue), Shortest Path
# Link     : https://leetcode.com/problems/minimum-time-to-reach-target-with-limited-power/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12380000 (beats 0%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import heapq

class Solution(object):
    def minTimeMaxPower(self, n, edges, power, cost, source, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type power: int
        :type cost: List[int]
        :type source: int
        :type target: int
        :rtype: List[int]
        """
        if source == target:
            return [0, power]
            
        graph = [[] for _ in range(n)]
        for u, v, t in edges:
            graph[u].append((v, t))
            
        dist = [[float('inf')] * (power + 1) for _ in range(n)]
        dist[source][power] = 0
        
        pq = [(0, -power, source)]
        
        while pq:
            curr_time, neg_p, u = heapq.heappop(pq)
            p = -neg_p
            
            if curr_time > dist[u][p]:
                continue
                
            if u == target:
                return [curr_time, p]
                
            if p >= cost[u]:
                next_p = p - cost[u]
                for v, t in graph[u]:
                    if curr_time + t < dist[v][next_p]:
                        dist[v][next_p] = curr_time + t
                        heapq.heappush(pq, (curr_time + t, -next_p, v))
                        
        return [-1, -1]