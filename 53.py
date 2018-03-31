class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        max_single = float('-inf')
        pre_yes = 0
        pre_no = 0
        for e in nums:
            pre_yes, pre_no = max(0, pre_yes+e), max(pre_yes, pre_no)
            if e > max_single:
                max_single = e
        temp = max(pre_yes, pre_no) 
        if temp == 0:
            return max_single
        return temp
