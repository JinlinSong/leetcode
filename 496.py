class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        temp = []
        for i, e in enumerate(nums1):
            temp.append(next((j for j in nums2[nums2.index(e)+1:] if j > e),-1))
        return temp
            
                    
