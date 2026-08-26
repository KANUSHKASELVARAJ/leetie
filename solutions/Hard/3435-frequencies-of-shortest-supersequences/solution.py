# ──────────────────────────────────────────────────
# Problem  : 3435. Frequencies of Shortest Supersequences
# Difficulty: Hard
# Tags     : Array, String, Bit Manipulation, Graph Theory, Topological Sort, Enumeration
# Link     : https://leetcode.com/problems/frequencies-of-shortest-supersequences/
# Runtime  : 4908 ms (beats 0%)
# Memory   : 14444000 (beats 0%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def supersequences(self, words):
        chars = sorted(list(set("".join(words))))
        k = len(chars)
        char_map = {c: i for i, c in enumerate(chars)}
        
        adj = [0] * k
        for word in words:
            if len(word) == 2:
                u, v = char_map[word[0]], char_map[word[1]]
                adj[u] |= (1 << v)

        valid_masks = []
        min_cardinality = k

        for mask in range(1 << k):
            cardinality = bin(mask).count('1')
            if cardinality > min_cardinality:
                continue

            in_degree = [0] * k
            for i in range(k):
                if not (mask & (1 << i)):
                    for j in range(k):
                        if not (mask & (1 << j)) and (adj[i] & (1 << j)):
                            in_degree[j] += 1

            queue = [i for i in range(k) if not (mask & (1 << i)) and in_degree[i] == 0]
            visited_count = 0
            
            while queue:
                u = queue.pop(0)
                visited_count += 1
                for v in range(k):
                    if not (mask & (1 << v)) and (adj[u] & (1 << v)):
                        in_degree[v] -= 1
                        if in_degree[v] == 0:
                            queue.append(v)

            once_nodes_count = k - cardinality
            if visited_count == once_nodes_count:
                if cardinality < min_cardinality:
                    min_cardinality = cardinality
                    valid_masks = [mask]
                elif cardinality == min_cardinality:
                    valid_masks.append(mask)

        ans = []
        for mask in valid_masks:
            freq = [0] * 26
            for i, c in enumerate(chars):
                idx = ord(c) - ord('a')
                freq[idx] = 2 if (mask & (1 << i)) else 1
            ans.append(freq)

        return ans