class Solution(object):
    def findRelativeRanks(self, nums):
        sort = sorted(nums)[::-1]
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(map(str, range(4, len(nums) + 1)))
        return list(map(dict(zip(sort, rank)).get, nums))
