# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        temp_a = headA
        temp_b = headB
        while temp_a != temp_b:
            if not temp_a:
                temp_a = headB
            if not temp_b:
                temp_b = headA
            temp_a = temp_a.next
            temp_b = temp_b.next
        return temp_a
        