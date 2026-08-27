# ──────────────────────────────────────────────────
# Problem  : 86. Partition List
# Difficulty: Medium
# Tags     : Linked List, Two Pointers
# Link     : https://leetcode.com/problems/partition-list/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12464000 (beats 0%)
# Language : python
# Copyright: (c) 2026 KANUSHKASELVARAJ. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head, x):
        before_head = ListNode(0)
        after_head = ListNode(0)
        
        before = before_head
        after = after_head
        
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
            
        # Terminate the after list to prevent cycles
        after.next = None
        
        # Connect before list to after list
        before.next = after_head.next
        
        return before_head.next