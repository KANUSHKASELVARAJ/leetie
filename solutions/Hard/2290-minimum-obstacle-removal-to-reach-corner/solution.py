# ──────────────────────────────────────────────────
# Problem  : 2290. Minimum Obstacle Removal to Reach Corner
# Difficulty: Hard
# Tags     : Array, Breadth-First Search, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path, 0-1 BFS, Dijkstra's Algorithm
# Link     : https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/
# Runtime  : 1816 ms (beats 49%)
# Memory   : 43896000 (beats 76%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import heapq
class Solution(object):
    def minimumObstacles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        dist=[[float('inf')]*n for _ in range(m)]
        dist[0][0]=0
        pq=[(0,0,0)]
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while pq:
            cost,row,col=heapq.heappop(pq)
            if row==m-1 and col==n-1:
                return cost
            if cost>dist[row][col]:
                continue
            for dr,dc in directions:
                nr=row+dr
                nc=col+dc
                if 0<=nr<m and 0<=nc<n:
                    newcost=cost+grid[nr][nc]
                    if newcost<dist[nr][nc]:
                        dist[nr][nc]=newcost
                        heapq.heappush(pq,(newcost,nr,nc))
        return dist[m-1][n-1]

        