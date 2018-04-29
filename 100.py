# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and not q:
            return False
        if not p and q:
            return False
        if not p and not q:
            return True
        if p.val != q.val:
            return False
        elif not self.isSameTree(p.left, q.left):
            return False  
        elif not self.isSameTree(p.right, q.right):
            return False
        return True
