# ──────────────────────────────────────────────────
# Problem  : 91. Decode Ways
# Difficulty: Medium
# Tags     : String, Dynamic Programming
# Link     : https://leetcode.com/problems/decode-ways/
# Runtime  : 1 ms (beats 57%)
# Memory   : 12460000 (beats 29%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
            
        # prev2 represents dp[i-2], prev1 represents dp[i-1]
        prev2, prev1 = 1, 1
        
        for i in range(1, len(s)):
            curr = 0
            
            # Single-digit check
            if s[i] != '0':
                curr += prev1
                
            # Two-digit check
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                curr += prev2
                
            prev2, prev1 = prev1, curr
            
        return prev1