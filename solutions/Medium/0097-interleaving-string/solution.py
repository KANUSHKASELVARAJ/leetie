# ──────────────────────────────────────────────────
# Problem  : 97. Interleaving String
# Difficulty: Medium
# Tags     : String, Dynamic Programming
# Link     : https://leetcode.com/problems/interleaving-string/
# Runtime  : 15 ms (beats 0%)
# Memory   : 12284000 (beats 0%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def isInterleave(self, s1, s2, s3):
        m, n = len(s1), len(s2)
        
        # Length check
        if m + n != len(s3):
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # Base case: first column (using only s1)
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        # Base case: first row (using only s2)
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        # Fill DP grid
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                from_s1 = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                from_s2 = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                dp[i][j] = from_s1 or from_s2

        return dp[m][n]