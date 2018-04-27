class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n =  len(s)
        count = 0
        for i in range(n):
            step = 1
            while i - step >= 0 and i + step < n and s[i - step] == s[i + step]:
                count += 1
                step += 1
            step = 1
            while i - step + 1 >= 0 and i + step < n and s[i - step + 1] == s[i + step]:
                count += 1
                step += 1
        return count + n

def test_run():
    a = Solution()
    b = a.countSubstrings('aaa')
    print(b)
    
if __name__ == "__main__":
    test_run()
