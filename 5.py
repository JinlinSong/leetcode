class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        L = len(s)
        temp = self.longest(s, 0)
        for i in range(1,L):
            temp_2 = self.longest(s, i)
            if len(temp_2) > len(temp):
                temp = temp_2
        return temp

    def longest(self, s, i):
        L = len(s)
        temp_1 = 1
        step = 1
        while i - step >= 0 and i + step < L and s[i - step] == s[i + step]:
            temp_1 += 2
            step += 1
        step -= 1
        temp_2 = 0
        step_2 = 1
        while i - step_2 + 1 >= 0 and i + step_2 < L and s[i - step_2 + 1] == s[i + step_2]:
            temp_2 += 2
            step_2 += 1
        step_2 -= 1
        if temp_2 >= temp_1:
            return s[(i - step_2 + 1):(i + step_2 + 1)]
        return s[(i - step):(i + step + 1)]
