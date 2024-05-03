#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pPath = []
        qPath = []

        # If outbounds then obviously there is a split
        def search(root, path, key):
            if not root: return
            path.append(root)
            if root == key: return
            if key.val < root.val:
                search(root.left, path, key)
            elif key.val > root.val:
                search(root.right, path, key)

        search(root, pPath, p)
        search(root, qPath, q)

        for i in range(max(len(pPath), len(qPath))):
            try:
                if pPath[i] != qPath[i]: return pPath[i - 1]
            except: return pPath[i - 1]

        
# @lc code=end

