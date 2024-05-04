#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Two ways.

        # use BFS to find each level of trees, and then add it for each level.

        # This way

        heightArray = []
        def traverse(node, level):
            if not node: return
            if level == len(heightArray):
                heightArray.append([])

            heightArray[level].append(node.val)

            traverse(node.left, level + 1)
            traverse(node.right, level + 1)

        traverse(root, 0)

        return heightArray
        
# @lc code=end

