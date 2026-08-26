# ──────────────────────────────────────────────────
# Problem  : 3244. Shortest Distance After Road Addition Queries II
# Difficulty: Hard
# Tags     : Array, Greedy, Graph Theory, Ordered Set
# Link     : https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12340000 (beats 0%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def shortestDistanceAfterQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        parent = list(range(n))

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        current_distance = n - 1
        ans = []

        for u, v in queries:
            # Find the actual active boundaries after applying existing shortcuts
            u_root = find(u)
            v_root = find(v)

            # Skip if the edge is contained within an already bypassed segment
            if u_root < v_root:
                curr = u_root
                while curr < v:
                    nxt = find(curr + 1)
                    parent[curr] = v_root
                    current_distance -= 1
                    curr = nxt

            ans.append(current_distance)

        return ans