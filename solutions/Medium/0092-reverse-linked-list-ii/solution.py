# ──────────────────────────────────────────────────
# Problem  : 92. Reverse Linked List II
# Difficulty: Medium
# Tags     : Linked List
# Link     : https://leetcode.com/problems/reverse-linked-list-ii/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12604000 (beats 45%)
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
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        # Step 1: Reach node just before position `left`
        for _ in range(left - 1):
            prev = prev.next

        # Step 2: Reverse sublist in-place
        curr = prev.next
        for _ in range(right - left):
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt

        return dummy.next