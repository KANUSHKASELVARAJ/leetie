# ──────────────────────────────────────────────────
# Problem  : 4003. Minimum Cost Path with Alternating Directions III
# Difficulty: Hard
# Tags     : Array, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path
# Link     : https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-iii/
# Runtime  : 4087 ms (beats 92%)
# Memory   : 63248000 (beats 11%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import heapq

class Solution(object):
    def minCost(self, m, n, penalty):
        """
        :type m: int
        :type n: int
        :type penalty: List[List[int]]
        :rtype: int
        """
        directions = ((1, 1, 0), (1, 0, 1), (0, -1, 0), (0, 0, -1))
        dist = [[[float('inf')] * n for _ in range(m)] for _ in range(2)]
        
        dist[0][0][0] = 1
        min_heap = [(1, 0, 0, 0)]
        
        while min_heap:
            w, p, i, j = heapq.heappop(min_heap)
            
            if w > dist[p][i][j]:
                continue
                
            if i == m - 1 and j == n - 1:
                return w
                
            if w + penalty[i][j] < dist[p ^ 1][i][j]:
                dist[p ^ 1][i][j] = w + penalty[i][j]
                heapq.heappush(min_heap, (dist[p ^ 1][i][j], p ^ 1, i, j))
                
            for dp, di, dj in directions:
                np, ni, nj = p ^ 1, i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    extra = penalty[i][j] if np != dp else 0
                    new_w = w + (ni + 1) * (nj + 1) + extra
                    if new_w < dist[np][ni][nj]:
                        dist[np][ni][nj] = new_w
                        heapq.heappush(min_heap, (new_w, np, ni, nj))
                        
        return -1