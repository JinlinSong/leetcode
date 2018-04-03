class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cmin = 0
        cmax = 0
        for e in s:
            if e == '(':
                cmin += 1
                cmax += 1
            elif e == '*':
                cmin = max(0, cmin - 1)
                cmax += 1
            elif e == ')':
                cmin = max(0, cmin - 1)
                cmax -= 1
            while cmax < 0:
                return False
        if cmin== 0:
            return True
        return False
