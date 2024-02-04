#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # General is idea is to have two pointers then seperated them by n.
        # As the last pointer will reach the end which then let first pointer to be able remove the value
        # Because the last point is n lengths away from the first.

        left, right = head, head
        for _ in range(n): right = right.next

        if not right: return head.next
        while right.next:
            left = left.next
            right = right.next

        left.next = left.next.next
        return head


# @lc code=end

