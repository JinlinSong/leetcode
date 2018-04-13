### iteratively
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        if not root:
            return res
        stack  = [root]
        while stack:
            curr = stack.pop()
            if not curr.left and not curr.right:
                res = res + [curr.val]
            else:
                stack = stack + [curr]
            if curr.right:
                stack = stack + [curr.right]
                curr.right = None
            if curr.left:
                stack = stack + [curr.left]
                curr.left = None
        return res
        
### Recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        res = self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        return res
