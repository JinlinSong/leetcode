class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        L = len(nums)
        result = set()
        for i in range(L - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, L-1
            while j < k:
                diff_temp = (nums[i] + nums[j] + nums[k])
                if diff_temp == 0:
                    result.add((nums[i], nums[j], nums[k]))
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                elif diff_temp < 0:
                    j += 1
                else:
                    k -= 1
        return [list(i) for i in result]
