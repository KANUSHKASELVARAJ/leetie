# ──────────────────────────────────────────────────
# Problem  : 93. Restore IP Addresses
# Difficulty: Medium
# Tags     : String, Backtracking
# Link     : https://leetcode.com/problems/restore-ip-addresses/
# Runtime  : 4 ms (beats 54%)
# Memory   : 12548000 (beats 1%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def restoreIpAddresses(self, s):
        result = []
        n = len(s)
        
        # An IP address cannot have fewer than 4 or more than 12 digits
        if n < 4 or n > 12:
            return result
            
        def backtrack(start, dots, current_ip):
            # Base case: placed 3 dots (4 segments)
            if dots == 4:
                if start == n:
                    result.append(".".join(current_ip))
                return
                
            # Remaining segments needed including current one
            remaining_dots = 4 - dots
            remaining_chars = n - start
            
            # Early pruning
            if remaining_chars < remaining_dots or remaining_chars > remaining_dots * 3:
                return
                
            for length in range(1, 4):
                if start + length > n:
                    break
                    
                segment = s[start:start + length]
                
                # Check for leading zero
                if len(segment) > 1 and segment[0] == '0':
                    break
                    
                # Check value range
                if int(segment) <= 255:
                    current_ip.append(segment)
                    backtrack(start + length, dots + 1, current_ip)
                    current_ip.pop()
                    
        backtrack(0, 0, [])
        return result