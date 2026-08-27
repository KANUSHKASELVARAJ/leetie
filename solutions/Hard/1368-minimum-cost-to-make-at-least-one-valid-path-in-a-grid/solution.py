# ──────────────────────────────────────────────────
# Problem  : 1368. Minimum Cost to Make at Least One Valid Path in a Grid
# Difficulty: Hard
# Tags     : Array, Breadth-First Search, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path, 0-1 BFS, Dijkstra's Algorithm
# Link     : https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/
# Runtime  : 191 ms (beats 26%)
# Memory   : 13116000 (beats 66%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import heapq
class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        dist=[[float('inf')]*n for _ in range(m)]
        dist[0][0]=0
        pq=[(0,0,0)]
        directions=[ (0, 1),(0, -1), (1, 0),(-1,0)]
        while pq:
            cost,r,c=heapq.heappop(pq)
            if cost>dist[r][c]:
                continue
            if r==m-1 and c==n-1:
                return cost
            for i,(dr,dc) in enumerate(directions):
                nr=dr+r
                nc=dc+c
                if 0<=nr<m and 0<=nc<n:
                    if grid[r][c]==i+1:
                        newcost=cost
                    else:
                        newcost=cost+1
                    if newcost<dist[nr][nc]:
                        dist[nr][nc]=newcost
                        heapq.heappush(pq,(newcost,nr,nc))
        return dist[m-1][n-1]
        