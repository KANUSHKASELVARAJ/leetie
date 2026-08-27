# ──────────────────────────────────────────────────
# Problem  : 3924. Minimum Threshold Path With Limited Heavy Edges
# Difficulty: Hard
# Tags     : Binary Search, Breadth-First Search, Graph Theory
# Link     : https://leetcode.com/problems/minimum-threshold-path-with-limited-heavy-edges/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12512000 (beats 0%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import heapq

class Solution:
    def minimumThreshold(self, n, edges, source, target, k):
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def can_reach(threshold):
            dist = [float('inf')] * n
            dist[source] = 0
            pq = [(0, source)]

            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]:
                    continue
                if u == target:
                    return d <= k

                for v, w in graph[u]:
                    if w <= threshold:
                        if d + w < dist[v]:
                            dist[v] = d + w
                            heapq.heappush(pq, (dist[v], v))

            return dist[target] <= k

        low, high = 0, 10**9
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            if can_reach(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans