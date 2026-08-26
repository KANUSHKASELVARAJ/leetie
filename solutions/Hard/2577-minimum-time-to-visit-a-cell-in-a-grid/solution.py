# ──────────────────────────────────────────────────
# Problem  : 2577. Minimum Time to Visit a Cell In a Grid
# Difficulty: Hard
# Tags     : Array, Breadth-First Search, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path
# Link     : https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/
# Runtime  : 998 ms (beats 97%)
# Memory   : 23620000 (beats 72%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import heapq

class Solution:
    def minimumTime(self, grid):
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        m, n = len(grid), len(grid[0])
        pq = [(0, 0, 0)]  # (time, row, col)
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while pq:
            t, r, c = heapq.heappop(pq)

            if r == m - 1 and c == n - 1:
                return t

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    if grid[nr][nc] <= t + 1:
                        heapq.heappush(pq, (t + 1, nr, nc))
                    else:
                        diff = grid[nr][nc] - t
                        if diff % 2 == 1:
                            heapq.heappush(pq, (grid[nr][nc], nr, nc))
                        else:
                            heapq.heappush(pq, (grid[nr][nc] + 1, nr, nc))

        return -1