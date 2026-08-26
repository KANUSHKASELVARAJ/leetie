# ──────────────────────────────────────────────────
# Problem  : 3547. Maximum Sum of Edge Values in a Graph
# Difficulty: Hard
# Tags     : Math, Greedy, Graph Theory
# Link     : https://leetcode.com/problems/maximum-sum-of-edge-values-in-a-graph/
# Runtime  : 522 ms (beats 33%)
# Memory   : 35384000 (beats 33%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def maxScore(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        cycle_sizes = []
        path_sizes = []
        seen = set()

        def get_component(start):
            component = [start]
            seen.add(start)
            for u in component:
                for v in graph[u]:
                    if v not in seen:
                        component.append(v)
                        seen.add(v)
            return component

        for i in range(n):
            if i not in seen:
                comp = get_component(i)
                if all(len(graph[u]) == 2 for u in comp):
                    cycle_sizes.append(len(comp))
                elif len(comp) > 1:
                    path_sizes.append(len(comp))

        def calculate_score(left, right, is_cycle):
            window = collections.deque([right, right])
            score = 0
            for val in range(right - 1, left - 1, -1):
                win_val = window.popleft()
                score += win_val * val
                window.append(val)
            
            if is_cycle:
                score += window.popleft() * window.popleft()
            return score

        ans = 0

        # Allocate highest available values to cycles first
        for size in cycle_sizes:
            ans += calculate_score(n - size + 1, n, True)
            n -= size

        # Allocate remaining values to paths sorted by size descending
        for size in sorted(path_sizes, reverse=True):
            ans += calculate_score(n - size + 1, n, False)
            n -= size

        return ans
        