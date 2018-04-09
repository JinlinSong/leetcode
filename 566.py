class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        temp = []
        for e in nums:
           temp = temp + e
        new = []
        if r*c != len(temp):
            return nums
        for i in range(r):
            new.append(temp[i*c:(i+1)*c])
        return new 
