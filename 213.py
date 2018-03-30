class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Bottom-up
        if len(nums) == 1:
            return nums[0]
        p_0 = 0
        pp_0 = 0
        for i in range(1,len(nums)):
            p_0, pp_0 = max(pp_0 + nums[i], p_0), p_0
            
        p_1 = 0
        pp_1 = 0
        for i in range(len(nums) - 1):
            p_1, pp_1 = max(pp_1 + nums[i], p_1), p_1
        
        return max(p_0, p_1)