# ──────────────────────────────────────────────────
# Problem  : 3710. Maximum Partition Factor
# Difficulty: Hard
# Tags     : Array, Binary Search, Depth-First Search, Breadth-First Search, Union-Find, Graph Theory
# Link     : https://leetcode.com/problems/maximum-partition-factor/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12612000 (beats 0%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def maxPartitionFactor(self, points):
        n = len(points)
        if n <= 2:
            return 0
        
        def dist(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        low = 0
        high = 4 * 10**9
        ans = 0

        def is_bipartite(d):
            color = {}
            for i in range(n):
                if i not in color:
                    color[i] = 0
                    stack = [i]
                    while stack:
                        u = stack.pop()
                        for v in range(n):
                            if u != v and dist(u, v) < d:
                                if v not in color:
                                    color[v] = 1 - color[u]
                                    stack.append(v)
                                elif color[v] == color[u]:
                                    return False
            return True

        while low <= high:
            mid = (low + high) // 2
            if is_bipartite(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans