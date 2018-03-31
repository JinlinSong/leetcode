class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        a, z = 0, len(nums) - 1
        if z < 0:
            return 0
        if target > nums[z]:
            return z + 1
        while a < z:
            m = int((a+z) / 2)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                a = m + 1
            else:
                z = m
        return a
                        
        
