# ──────────────────────────────────────────────────
# Problem  : 3898. Find the Degree of Each Vertex
# Difficulty: Easy
# Tags     : Array, Graph Theory, Matrix
# Link     : https://leetcode.com/problems/find-the-degree-of-each-vertex/
# Runtime  : 47 ms (beats 5%)
# Memory   : 12740000 (beats 10%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = len(matrix)
        degrees = [0] * n
        
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1:
                    degrees[i] += 1
                    
        return degrees