# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # top-down
        def double_rob(root):
            if not root:
                return (0,0)
            left = double_rob(root.left)
            right = double_rob(root.right)
            return (max(left) + max(right), root.val + left[0] + right[0])
        return max(double_rob(root))