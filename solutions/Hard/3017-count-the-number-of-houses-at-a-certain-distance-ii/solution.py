# ──────────────────────────────────────────────────
# Problem  : 3017. Count the Number of Houses at a Certain Distance II
# Difficulty: Hard
# Tags     : Graph Theory, Prefix Sum
# Link     : https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-ii/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12352000 (beats 0%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def countOfPairs(self, n, x, y):
        if x > y:
            x, y = y, x

        diff = [0] * (n + 2)

        def add_range(l, r, val):
            if l <= r:
                diff[l] += val
                diff[r + 1] -= val

        for i in range(1, n + 1):
            if x == y or abs(x - y) <= 1:
                # Direct distance without cycle shortcut
                add_range(1, i - 1, 1)
                add_range(1, n - i, 1)
            else:
                # 1. Nodes strictly to the left of i
                add_range(1, i - 1, 1)

                # 2. Nodes to the right of i: compare direct distance vs shortcut via (x, y)
                # Case A: i is to the left of x (i <= x)
                if i <= x:
                    # Direct path is shorter or equal up to mid point
                    # d_direct = j - i
                    # d_shortcut = (x - i) + 1 + (y - j)
                    # d_shortcut < d_direct => 2*j > i + y + x - 1
                    split = (i + y + x) // 2
                    
                    # For j in [i + 1, split]: use direct path
                    add_range(1, max(0, split - i), 1)

                    # For j in [split + 1, n]: use shortcut path
                    # d = (x - i) + 1 + |y - j|
                    base_dist = (x - i) + 1
                    
                    # j in [split + 1, y]
                    l1, r1 = split + 1, min(n, y)
                    if l1 <= r1:
                        d_max = base_dist + (y - l1)
                        d_min = base_dist + (y - r1)
                        add_range(d_min, d_max, 1)

                    # j in [y + 1, n]
                    l2, r2 = max(split + 1, y + 1), n
                    if l2 <= r2:
                        d_min = base_dist + (l2 - y)
                        d_max = base_dist + (r2 - y)
                        add_range(d_min, d_max, 1)

                # Case B: i is inside the cycle/shortcut interval [x + 1, y - 1]
                elif i < y:
                    # Distance to j > i
                    for j_start, j_end in [(i + 1, y), (y + 1, n)]:
                        if j_start > n:
                            continue
                        j_end = min(n, j_end)
                        if j_start > j_end:
                            continue

                        # Calculate min distance to each node in this range
                        for j in range(j_start, j_end + 1):
                            d1 = j - i
                            d2 = (i - x) + 1 + abs(y - j)
                            d3 = (y - i) + 1 + abs(x - j)
                            dist = min(d1, d2, d3)
                            diff[dist] += 1
                            diff[dist + 1] -= 1

                # Case C: i is to the right of y (i >= y)
                else:
                    # Symmetric to i <= x, simple linear distances
                    add_range(1, n - i, 1)

        ans = [0] * n
        curr = 0
        for i in range(1, n + 1):
            curr += diff[i]
            ans[i - 1] = curr

        return ans