class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        temp = []
        while nums1 or nums2:
            if not nums1:
                temp += nums2
                nums2 = []
            if not nums2:
                temp += nums1
                nums1 = []
            if nums1 and nums2:
                temp1 = nums1[0]
                temp2 = nums2[0]
                if temp1 > temp2:
                    temp.append(temp2)
                    nums2.remove(temp2)
                elif temp1 < temp2:
                    temp.append(temp1)
                    nums1.remove(temp1)
                else:
                    temp.append(temp1)
                    temp.append(temp1)
                    nums1.remove(temp1)
                    nums2.remove(temp1)
        nums1 = temp[-(m+n):]       
        print(nums1)
        