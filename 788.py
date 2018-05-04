class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        # Brute - Force solution
        count = 0
        for i in range(1, N+1):
            temp = str(i)
            if '3' in temp or '4' in temp or '7' in temp:
                continue
            if '2'in temp or '5' in temp or '6' in temp or '9' in temp:
                count += 1
        return count
