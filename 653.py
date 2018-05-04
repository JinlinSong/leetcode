# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        root_list = self.convert_to_list(root)
        i = 0
        j = len(root_list) - 1
        while i < j:
            if root_list[i] + root_list[j] == k:
                return True
            if root_list[i] + root_list[j] > k:
                j -= 1
            else:
                i += 1
        return False
        
    def convert_to_list(self, root):
        if not root:
            return []
        return self.convert_to_list(root.left) + [root.val] + self.convert_to_list(root.right)
        
