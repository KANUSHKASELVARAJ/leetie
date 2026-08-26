# ──────────────────────────────────────────────────
# Problem  : 3534. Path Existence Queries in a Graph II
# Difficulty: Hard
# Tags     : Array, Two Pointers, Binary Search, Dynamic Programming, Greedy, Bit Manipulation, Graph Theory, Sorting
# Link     : https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12304000 (beats 0%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        sorted_nodes = sorted((num, i) for i, num in enumerate(nums))
        sorted_vals = [val for val, _ in sorted_nodes]
        
        # Map original node indices to sorted indices
        pos = [0] * n
        for sorted_idx, (_, orig_idx) in enumerate(sorted_nodes):
            pos[orig_idx] = sorted_idx

        # Step 2: Compute farthest right jump for each sorted position using two-pointer sweep
        max_level = n.bit_length() + 1
        jump = [[0] * max_level for _ in range(n)]
        
        r = 0
        for i in range(n):
            while r + 1 < n and sorted_vals[r + 1] - sorted_vals[i] <= maxDiff:
                r += 1
            jump[i][0] = r

        # Step 3: Build Binary Lifting table
        for level in range(1, max_level):
            for i in range(n):
                jump[i][level] = jump[jump[i][level - 1]][level - 1]

        # Step 4: Answer queries in O(log N) time
        ans = []
        for u, v in queries:
            start, end = min(pos[u], pos[v]), max(pos[u], pos[v])
            
            if start == end:
                ans.append(0)
                continue
                
            steps = 0
            curr = start
            
            # Jump as far as possible without reaching or exceeding 'end'
            for level in range(max_level - 1, -1, -1):
                if jump[curr][level] < end:
                    curr = jump[curr][level]
                    steps += (1 << level)
            
            # Check if one final jump can reach 'end'
            if jump[curr][0] >= end:
                ans.append(steps + 1)
            else:
                ans.append(-1)

        return ans
        