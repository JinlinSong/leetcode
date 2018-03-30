class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Bottom-up
        pp = 0
        p = 0
        for i in range(len(nums)):
            p, pp = max(pp + nums[i], p), p
        return p