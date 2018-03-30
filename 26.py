class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        before = nums[0]
        i = 1
        for e in range(1, len(nums)):
            print(nums[e])
            if nums[e] == before:
                pass
            else:
                i += 1
                nums[i-1] = nums[e]
                before = nums[e]
            print(nums)
        return i