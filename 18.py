class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        L = len(nums)
        result = set()
        for i in range(L - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for s in range(i+1, L - 2):
                if s > i + 1 and nums[s] == nums[s-1]:
                    continue
                j, k = s+1, L-1
                while j < k:
                    diff_temp = (nums[i] + nums[s] + nums[j] + nums[k])
                    if diff_temp == target:
                        result.add((nums[i], nums[s], nums[j], nums[k]))
                        while j < k and nums[j] == nums[j + 1]:
                            j += 1
                        while j < k and nums[k] == nums[k - 1]:
                            k -= 1
                        j += 1
                    elif diff_temp < target:
                        j += 1
                    else:
                        k -= 1
        return [list(i) for i in result]
