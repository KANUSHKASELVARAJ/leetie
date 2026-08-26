# ──────────────────────────────────────────────────
# Problem  : 3543. Maximum Weighted K-Edge Path
# Difficulty: Medium
# Tags     : Hash Table, Dynamic Programming, Graph Theory
# Link     : https://leetcode.com/problems/maximum-weighted-k-edge-path/
# Runtime  : 483 ms (beats 100%)
# Memory   : 33140000 (beats 0%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import defaultdict
class Solution(object):
    def maxWeight(self, n, edges, k, t):
        """
        :type n: int
        :type edges: List[List[int]]
        :type k: int
        :type t: int
        :rtype: int
        """
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            
        # dp[u][i] stores the set of reachable path sums ending at node u using i edges
        dp = [defaultdict(set) for _ in range(n)]
        
        # Base case: 0 edges used starting at any node u has a path sum of 0
        for u in range(n):
            dp[u][0].add(0)
            
        # Transitions over number of edges used
        for i in range(k):
            for u in range(n):
                if i in dp[u]:
                    for curr_sum in dp[u][i]:
                        for v, w in graph[u]:
                            new_sum = curr_sum + w
                            if new_sum < t:
                                dp[v][i + 1].add(new_sum)
                                
        # Find the maximum valid sum ending at any node after exactly k steps
        ans = -1
        for u in range(n):
            if k in dp[u] and dp[u][k]:
                ans = max(ans, max(dp[u][k]))
                
        return ans
        