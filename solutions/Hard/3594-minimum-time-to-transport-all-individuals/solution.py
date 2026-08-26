# ──────────────────────────────────────────────────
# Problem  : 3594. Minimum Time to Transport All Individuals
# Difficulty: Hard
# Tags     : Array, Bit Manipulation, Graph Theory, Heap (Priority Queue), Shortest Path, Bitmask
# Link     : https://leetcode.com/problems/minimum-time-to-transport-all-individuals/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12608000 (beats 0%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import heapq
from math import floor
from itertools import combinations

class Solution:
    def minTime(self, n, k, m, time, mul):
        target_mask = (1 << n) - 1
        
        dist = {}
        pq = [(0.0, 0, 0)]
        dist[(0, 0)] = 0.0

        while pq:
            d, mask, stage = heapq.heappop(pq)

            if d > dist.get((mask, stage), float('inf')):
                continue

            if mask == target_mask:
                return d

            base_people = [i for i in range(n) if not (mask & (1 << i))]
            
            for g_size in range(1, min(k, len(base_people)) + 1):
                for group in combinations(base_people, g_size):
                    max_time = max(time[i] for i in group)
                    cross_cost = max_time * mul[stage]
                    next_stage = (stage + int(floor(cross_cost))) % m
                    
                    new_mask = mask
                    for p in group:
                        new_mask |= (1 << p)

                    if new_mask == target_mask:
                        next_time = d + cross_cost
                        if next_time < dist.get((new_mask, next_stage), float('inf')):
                            dist[(new_mask, next_stage)] = next_time
                            heapq.heappush(pq, (next_time, new_mask, next_stage))
                    
                    else:
                        dest_people = [i for i in range(n) if (new_mask & (1 << i))]
                        for r in dest_people:
                            return_cost = time[r] * mul[next_stage]
                            after_return_stage = (next_stage + int(floor(return_cost))) % m
                            after_return_mask = new_mask ^ (1 << r)

                            next_time = d + cross_cost + return_cost
                            if next_time < dist.get((after_return_mask, after_return_stage), float('inf')):
                                dist[(after_return_mask, after_return_stage)] = next_time
                                heapq.heappush(pq, (next_time, after_return_mask, after_return_stage))

        return -1.0