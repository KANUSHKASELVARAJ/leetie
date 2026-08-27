# ──────────────────────────────────────────────────
# Problem  : 82. Remove Duplicates from Sorted List II
# Difficulty: Medium
# Tags     : Linked List, Two Pointers
# Link     : https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Runtime  : 3 ms (beats 49%)
# Memory   : 12392000 (beats 89%)
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
    def deleteDuplicates(self, head):
        dummy = ListNode(0, head)
        prev = dummy
        
        while head:
            # Check if current node is start of duplicate sequence
            if head.next and head.val == head.next.val:
                # Skip all nodes with the duplicate value
                while head.next and head.val == head.next.val:
                    head = head.next
                # Link prev to the node after the last duplicate
                prev.next = head.next
            else:
                # Node is unique, advance prev
                prev = prev.next
                
            head = head.next
            
        return dummy.next