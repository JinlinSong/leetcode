###iteratively
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        front = [root]
        while front:
            temp = front.pop()
            if temp:
                res.append(temp.val)
                front = front + [temp.right] + [temp.left]
        return res
   
###Recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        res = [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        return res
