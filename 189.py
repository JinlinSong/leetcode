class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            temp = [nums.pop()]
            temp = temp + nums
            nums = temp
            k -= 1
        return nums