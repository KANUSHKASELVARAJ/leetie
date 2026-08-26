# ──────────────────────────────────────────────────
# Problem  : 3311. Construct 2D Grid Matching Graph Layout
# Difficulty: Hard
# Tags     : Array, Hash Table, Graph Theory, Matrix
# Link     : https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12484000 (beats 0%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def constructGridLayout(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # Classify nodes by their degree
        deg = [-1] * 5
        for x, ys in enumerate(g):
            deg[len(ys)] = x

        # Step 1: Construct the first row of the grid
        if deg[1] != -1:
            # Case 1: 1D path (line graph), starting node has degree 1
            row = [deg[1]]
        elif deg[4] == -1:
            # Case 2: 2-column grid (no inner nodes with degree 4 exist)
            x = deg[2]
            for y in g[x]:
                if len(g[y]) == 2:
                    row = [x, y]
                    break
        else:
            # Case 3: Standard multi-row/multi-column 2D grid
            # Start from a corner node (degree 2) and traverse along an edge
            x = deg[2]
            row = [x]
            pre = x
            x = g[x][0]
            while len(g[x]) > 2:
                row.append(x)
                for y in g[x]:
                    if y != pre and len(g[y]) < 4:
                        pre = x
                        x = y
                        break
            row.append(x)

        # Step 2: Reconstruct subsequent rows using BFS/unvisited neighbor matching
        ans = [row]
        vis = [False] * n
        
        for _ in range(n // len(row) - 1):
            for x in row:
                vis[x] = True
            nxt = []
            for x in row:
                for y in g[x]:
                    if not vis[y]:
                        nxt.append(y)
                        break
            ans.append(nxt)
            row = nxt

        return ans
        