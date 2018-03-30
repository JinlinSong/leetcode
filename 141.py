# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        a = head.next
        if not a:
            return False
        temp = head.next if head.next else head
        b = temp.next
        if a == b:
            return True
        while a != b:
            a = a.next
            if not a.next:
                return False
            temp = b.next if b.next else head
            b = temp.next
            if a == b:
                return True
        return False