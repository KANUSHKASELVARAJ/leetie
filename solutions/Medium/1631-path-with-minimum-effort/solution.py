# ──────────────────────────────────────────────────
# Problem  : 1631. Path With Minimum Effort
# Difficulty: Medium
# Tags     : Array, Binary Search, Depth-First Search, Breadth-First Search, Union-Find, Heap (Priority Queue), Matrix, Dijkstra's Algorithm
# Link     : https://leetcode.com/problems/path-with-minimum-effort/
# Runtime  : 412 ms (beats 61%)
# Memory   : 13172000 (beats 81%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import heapq
class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        m=len(heights)
        n=len(heights[0])
        dist=[[float('inf')]*n for _ in range(m)]
        dist[0][0]=0
        pq=[(0,0,0)]
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while pq:
            effort,r,c=heapq.heappop(pq)
            if r==m-1 and c==n-1:
                return effort
            if effort>dist[r][c]:
                continue
            for dr,dc in directions:
                nr=dr+r
                nc=dc+c
                if 0<=nr<m and 0<=nc<n:
                    diff=abs(heights[r][c]-heights[nr][nc])
                    neweffort=max(diff,effort)
                    if neweffort<dist[nr][nc]:
                        dist[nr][nc]=neweffort
                        heapq.heappush(pq,(neweffort,nr,nc))
        return dist[m-1][n-1]
