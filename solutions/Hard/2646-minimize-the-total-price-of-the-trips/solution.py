# ──────────────────────────────────────────────────
# Problem  : 2646. Minimize the Total Price of the Trips
# Difficulty: Hard
# Tags     : Array, Dynamic Programming, Tree, Depth-First Search, Graph Theory
# Link     : https://leetcode.com/problems/minimize-the-total-price-of-the-trips/
# Runtime  : 55 ms (beats 60%)
# Memory   : 12664000 (beats 20%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import defaultdict

class Solution:
    def minimumTotalPrice(self, n, edges, price, trips):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        count = [0] * n

        def dfs_count(curr, parent, target):
            if curr == target:
                count[curr] += 1
                return True
            for neighbor in adj[curr]:
                if neighbor != parent:
                    if dfs_count(neighbor, curr, target):
                        count[curr] += 1
                        return True
            return False

        for start, end in trips:
            dfs_count(start, -1, end)

        def dfs_dp(curr, parent):
            no_halve = price[curr] * count[curr]
            halve = (price[curr] // 2) * count[curr]

            for neighbor in adj[curr]:
                if neighbor != parent:
                    child_no_halve, child_halve = dfs_dp(neighbor, curr)
                    no_halve += min(child_no_halve, child_halve)
                    halve += child_no_halve

            return no_halve, halve

        return min(dfs_dp(0, -1))