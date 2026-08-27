# ──────────────────────────────────────────────────
# Problem  : 3910. Count Connected Subgraphs with Even Node Sum
# Difficulty: Hard
# Tags     : Array, Bit Manipulation, Depth-First Search, Breadth-First Search, Union-Find, Graph Theory, Enumeration
# Link     : https://leetcode.com/problems/count-connected-subgraphs-with-even-node-sum/
# Runtime  : 424 ms (beats 11%)
# Memory   : 12784000 (beats 67%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def evenSumSubgraphs(self, nums, edges):
        n = len(nums)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        ans = 0
        total_subsets = 1 << n

        for mask in range(1, total_subsets):
            node_sum = sum(nums[i] for i in range(n) if (mask >> i) & 1)
            if node_sum % 2 != 0:
                continue

            start = (mask & -mask).bit_length() - 1
            visited_mask = 0
            
            queue = [start]
            visited_mask |= 1 << start

            while queue:
                u = queue.pop(0)
                for v in graph[u]:
                    if ((mask >> v) & 1) and not ((visited_mask >> v) & 1):
                        visited_mask |= 1 << v
                        queue.append(v)

            if visited_mask == mask:
                ans += 1

        return ans