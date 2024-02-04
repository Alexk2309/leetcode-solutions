#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findHeight(self, root):
        if not root: return 0

        leftHeight = self.findHeight(root.left) + 1
        rightHeight = self.findHeight(root.right) + 1

        return max(leftHeight, rightHeight)


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.findHeight(root)

# @lc code=end

