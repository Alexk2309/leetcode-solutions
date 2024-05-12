#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Idea is to have limits and you recursively so smaller and smaller.

        def valid(node, minValue, maxValue):
            if not node: return True
            if not (minValue < node.val and node.val < maxValue): return False
            return valid(node.left, minValue, node.val) and valid(node.right, node.val, maxValue)

        return valid(root, float('-inf'), float('inf'))

# @lc code=end›››

