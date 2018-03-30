class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length_needle = len(needle)
        length_haystack = len(haystack)
        if length_haystack < length_needle:
            return -1
        for i in range(length_haystack-length_needle+1):
            print(haystack[i:i+length_needle])
            if haystack[i:i+length_needle] == needle:
                return i
        return -1