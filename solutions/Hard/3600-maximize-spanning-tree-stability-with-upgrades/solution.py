# ──────────────────────────────────────────────────
# Problem  : 3600. Maximize Spanning Tree Stability with Upgrades
# Difficulty: Hard
# Tags     : Binary Search, Greedy, Union-Find, Graph Theory, Minimum Spanning Tree
# Link     : https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/
# Runtime  : 4218 ms (beats 10%)
# Memory   : 154592000 (beats 5%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def maxStability(self, n, edges, k):
        parent = list(range(n))
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i, root_j = find(i), find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                return True
            return False

        mandatory_min = float('inf')
        
        for u, v, s, must in edges:
            if must:
                if not union(u, v):
                    return -1
                mandatory_min = min(mandatory_min, s)

        full_parent = list(parent)
        for u, v, s, must in edges:
            if not must:
                union(u, v)

        if len({find(i) for i in range(n)}) > 1:
            return -1

        low = 1
        high = mandatory_min if mandatory_min != float('inf') else 200000
        ans = -1

        def check(lim):
            curr_parent = list(full_parent)

            def find_curr(i):
                if curr_parent[i] == i:
                    return i
                curr_parent[i] = find_curr(curr_parent[i])
                return curr_parent[i]

            def union_curr(i, j):
                root_i, root_j = find_curr(i), find_curr(j)
                if root_i != root_j:
                    curr_parent[root_i] = root_j
                    return True
                return False

            for u, v, s, must in edges:
                if not must and s >= lim:
                    union_curr(u, v)

            upgrades_left = k
            for u, v, s, must in edges:
                if not must and s < lim <= s * 2:
                    if upgrades_left > 0 and union_curr(u, v):
                        upgrades_left -= 1

            return len({find_curr(i) for i in range(n)}) == 1

        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans