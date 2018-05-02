class Solution(object):
    def countBinarySubstrings(self, s):
        s = [len(i) for i in s.replace('01', '0 1').replace('10', '1 0').split()]
        return sum(min(s[i-1], s[i]) for i in range(1, len(s)))
