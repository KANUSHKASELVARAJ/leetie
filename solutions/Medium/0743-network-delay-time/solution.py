# ──────────────────────────────────────────────────
# Problem  : 743. Network Delay Time
# Difficulty: Medium
# Tags     : Depth-First Search, Breadth-First Search, Graph Theory, Heap (Priority Queue), Shortest Path, Dijkstra's Algorithm
# Link     : https://leetcode.com/problems/network-delay-time/
# Runtime  : 352 ms (beats 80%)
# Memory   : 14804000 (beats 10%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph=[[] for _ in range(n+1)]
        for u,v,w in times:
            graph[u].append((v,w))
        dist=[float('inf')]*(n+1)
        dist[k]=0
        pq=[(0,k)]
        while pq:
            d,node=heapq.heappop(pq)
            if d>dist[node]:
                continue
            for nei,weight in graph[node]:
                newdist=d+weight
                if newdist<dist[nei]:
                    dist[nei]=newdist
                    heapq.heappush(pq,(newdist,nei))
        ans=max(dist[1:])
        if ans==float('inf'):
            return -1
        else:
            return ans


        