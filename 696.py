### method 1
class Solution(object):
    def countBinarySubstrings(self, s):
        s = [len(i) for i in s.replace('01', '0 1').replace('10', '1 0').split()]
        return sum(min(s[i-1], s[i]) for i in range(1, len(s)))

    
### method 2
class Solution(object):
    def countBinarySubstrings(self, s):
        cur_count = 1
        pre_count = 0
        ans = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur_count += 1
            else:
                ans += min(cur_count, pre_count)
                pre_count = cur_count
                cur_count = 1
        return ans + min(cur_count, pre_count)
                
                
