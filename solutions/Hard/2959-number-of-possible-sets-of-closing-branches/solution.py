# ──────────────────────────────────────────────────
# Problem  : 2959. Number of Possible Sets of Closing Branches
# Difficulty: Hard
# Tags     : Bit Manipulation, Graph Theory, Heap (Priority Queue), Enumeration, Shortest Path
# Link     : https://leetcode.com/problems/number-of-possible-sets-of-closing-branches/
# Runtime  : 1305 ms (beats 13%)
# Memory   : 12092000 (beats 100%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def numberOfSets(self, n, maxDistance, roads):
        ans = 0

        for mask in range(1 << n):
            dist = [[float('inf')] * n for _ in range(n)]
            for i in range(n):
                dist[i][i] = 0

            for u, v, w in roads:
                if (mask & (1 << u)) and (mask & (1 << v)):
                    dist[u][v] = min(dist[u][v], w)
                    dist[v][u] = min(dist[v][u], w)
            for k in range(n):
                if not (mask & (1 << k)):
                    continue
                for i in range(n):
                    if not (mask & (1 << i)):
                        continue
                    for j in range(n):
                        if not (mask & (1 << j)):
                            continue
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

           
            valid = True
            for i in range(n):
                if not (mask & (1 << i)):
                    continue
                for j in range(n):
                    if not (mask & (1 << j)):
                        continue
                    if dist[i][j] > maxDistance:
                        valid = False
                        break
                if not valid:
                    break

            if valid:
                ans += 1

        return ans