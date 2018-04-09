# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return None
        front = [root]
        ave_list = []
        while front:
            sum_level = 0
            count = len(front)
            front_ne = []
            for e in front:
                if e.left:
                    front_ne.append(e.left)
                if e.right:
                    front_ne.append(e.right)
                sum_level += e.val
            ave_list.append(sum_level/count)
            front = front_ne
        return ave_list
