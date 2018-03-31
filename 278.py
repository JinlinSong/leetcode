# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        start = 1
        end = n
        while start +1 < end:
            temp = int((start + end)/2)
            if isBadVersion(temp):
                end = temp
            else:
                start = temp
        return end
