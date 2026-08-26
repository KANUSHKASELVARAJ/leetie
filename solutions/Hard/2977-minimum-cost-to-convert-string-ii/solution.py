# ──────────────────────────────────────────────────
# Problem  : 2977. Minimum Cost to Convert String II
# Difficulty: Hard
# Tags     : Array, String, Dynamic Programming, Graph Theory, Trie, Shortest Path
# Link     : https://leetcode.com/problems/minimum-cost-to-convert-string-ii/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12448000 (beats 0%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def minimumCost(self, source, target, original, changed, cost):
        # Step 1: Map unique strings to integer IDs
        nodes = {}
        
        def get_id(s):
            if s not in nodes:
                nodes[s] = len(nodes)
            return nodes[s]

        for u, v in zip(original, changed):
            get_id(u)
            get_id(v)

        num_nodes = len(nodes)
        
        # Step 2: Build distance matrix using Floyd-Warshall
        dist = [[float('inf')] * num_nodes for _ in range(num_nodes)]
        for i in range(num_nodes):
            dist[i][i] = 0

        for u, v, w in zip(original, changed, cost):
            u_id, v_id = get_id(u), get_id(v)
            dist[u_id][v_id] = min(dist[u_id][v_id], w)

        for k in range(num_nodes):
            for i in range(num_nodes):
                for j in range(num_nodes):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        # Group valid replacements by length to optimize substring lookups
        length_to_substrips = {}
        for s, u_id in nodes.items():
            l = len(s)
            if l not in length_to_substrips:
                length_to_substrips[l] = set()
            length_to_substrips[l].add(s)

        unique_lengths = sorted(length_to_substrips.keys())

        # Step 3: Dynamic Programming
        n = len(source)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == float('inf'):
                continue

            # Case 1: Matching single characters without conversion
            if source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])

            # Case 2: Multi-character transformations matching stored patterns
            for length in unique_lengths:
                if i + length > n:
                    break

                sub_src = source[i:i + length]
                sub_tgt = target[i:i + length]

                if sub_src in nodes and sub_tgt in nodes:
                    u_id, v_id = nodes[sub_src], nodes[sub_tgt]
                    if dist[u_id][v_id] != float('inf'):
                        dp[i + length] = min(dp[i + length], dp[i] + dist[u_id][v_id])

        return dp[n] if dp[n] != float('inf') else -1