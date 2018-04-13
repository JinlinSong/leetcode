### iteratively
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        if not root:
            return res
        else:
            stack = stack + [root]
        while stack:
            curr = stack[-1]
            if curr.left:
                stack = stack + [curr.left]
                curr.left = None
            else:
                res = res + [curr.val]
                temp = curr.right
                stack.pop()
                if temp:
                    stack = stack + [temp]                    
        return res
        
### Recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        res = self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        return res
