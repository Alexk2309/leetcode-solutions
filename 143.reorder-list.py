#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:




    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Find middle of the list.

        slow = head
        fast = slow.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reversing seconf half
        curr = slow.next
        prev = slow.next = None
        while curr:
            tmp = curr
            curr = curr.next
            tmp.next = prev
            prev = tmp

        # Merge half
        half1 = head
        half2 = prev
        while half1 and half2:
            tmp1 = half1.next
            tmp2 = half2.next
            half1.next = half2
            half2.next = tmp1

            half1 = tmp1
            half2 = tmp2



# @lc code=end

