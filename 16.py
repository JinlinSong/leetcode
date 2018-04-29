class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        diff = float("inf")
        L = len(nums)
        result = None
        for i in range(L):
            j, k = i+1, L-1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                diff_temp = target - temp
                if diff_temp == 0:
                    return temp
                elif diff_temp > 0:
                    if diff_temp < diff:
                        diff = diff_temp
                        result = temp
                    j += 1
                else:
                    if - diff_temp < diff:
                        diff = - diff_temp
                        result = temp
                    k -= 1
        return result
