# ──────────────────────────────────────────────────
# Problem  : 2876. Count Visited Nodes in a Directed Graph
# Difficulty: Hard
# Tags     : Dynamic Programming, Depth-First Search, Graph Theory, Topological Sort, Memoization, Kosaraju's Algorithm, Tarjan's SCC Algorithm
# Link     : https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/
# Runtime  : 503 ms (beats 33%)
# Memory   : 56996000 (beats 27%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def countVisitedNodes(self, edges):
        n = len(edges)
        ans = [0] * n
        visited = [False] * n
        in_degree = [0] * n

        for v in edges:
            in_degree[v] += 1

        # Topological sort to filter out non-cycle nodes (trees attached to cycles)
        from collections import deque
        queue = deque([i for i in range(n) if in_degree[i] == 0])

        while queue:
            curr = queue.popleft()
            nxt = edges[curr]
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

        # Process cycle nodes
        for i in range(n):
            if in_degree[i] > 0 and not visited[i]:
                cycle = []
                curr = i
                while not visited[curr]:
                    visited[curr] = True
                    cycle.append(curr)
                    curr = edges[curr]
                
                cycle_len = len(cycle)
                for node in cycle:
                    ans[node] = cycle_len

        # Process tree nodes leading into cycles via DFS/recursion
        def dfs(u):
            if ans[u] > 0:
                return ans[u]
            ans[u] = 1 + dfs(edges[u])
            return ans[u]

        for i in range(n):
            if ans[i] == 0:
                dfs(i)

        return ans