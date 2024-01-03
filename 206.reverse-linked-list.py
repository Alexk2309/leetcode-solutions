#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head: return head

        prev = None
        curr = head
        while curr:
            tmp = curr
            # Iterate early so we can go the next node, without blocking it.
            curr = curr.next

            # Make previous current node point to prev
            tmp.next = prev

            # Change the prevous node to current Node.
            prev = tmp

        return prev
# @lc code=end

