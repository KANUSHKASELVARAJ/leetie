# ──────────────────────────────────────────────────
# Problem  : 3620. Network Recovery Pathways
# Difficulty: Hard
# Tags     : Array, Binary Search, Dynamic Programming, Graph Theory, Topological Sort, Heap (Priority Queue), Shortest Path
# Link     : https://leetcode.com/problems/network-recovery-pathways/
# Runtime  : 1487 ms (beats 64%)
# Memory   : 52100000 (beats 20%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import collections

class Solution:
    def findMaxPathScore(self, edges, online, k):
        n = len(online)
        graph = collections.defaultdict(list)
        indegree = [0] * n
        max_edge_weight = -1
        
        for u, v, w in edges:
            if online[u] and online[v]:
                graph[u].append((v, w))
                indegree[v] += 1
                if w > max_edge_weight:
                    max_edge_weight = w

        q = collections.deque([i for i in range(n) if indegree[i] == 0])
        topo_order = []
        while q:
            u = q.popleft()
            topo_order.append(u)
            for v, _ in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        def can_reach(min_w):
            dp = [float('inf')] * n
            dp[0] = 0
            
            for u in topo_order:
                if dp[u] > k:
                    continue
                for v, w in graph[u]:
                    if w >= min_w:
                        if dp[u] + w < dp[v]:
                            dp[v] = dp[u] + w
            
            return dp[n - 1] <= k

        low = 0
        high = max_edge_weight
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            if can_reach(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans