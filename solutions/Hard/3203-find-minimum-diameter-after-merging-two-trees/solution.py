# ──────────────────────────────────────────────────
# Problem  : 3203. Find Minimum Diameter After Merging Two Trees
# Difficulty: Hard
# Tags     : Tree, Depth-First Search, Breadth-First Search, Graph Theory
# Link     : https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/
# Runtime  : 619 ms (beats 92%)
# Memory   : 71732000 (beats 83%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def minimumDiameterAfterMerge(self, edges1, edges2):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :rtype: int
        """
        def get_diameter(edges):
            if not edges:
                return 0
            n = len(edges) + 1
            adj = [[] for _ in range(n)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)

            def bfs(start):
                dist = [-1] * n
                dist[start] = 0
                q = deque([start])
                farthest_node = start
                max_dist = 0

                while q:
                    u = q.popleft()
                    for v in adj[u]:
                        if dist[v] == -1:
                            dist[v] = dist[u] + 1
                            if dist[v] > max_dist:
                                max_dist = dist[v]
                                farthest_node = v
                            q.append(v)
                return farthest_node, max_dist

            node_a, _ = bfs(0)
            _, diameter = bfs(node_a)
            return diameter

        d1 = get_diameter(edges1)
        d2 = get_diameter(edges2)

        r1 = (d1 + 1) // 2
        r2 = (d2 + 1) // 2

        return max(d1, d2, r1 + r2 + 1)
        