class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = {}
        temp[1], temp[2] = 1, 2
        def climbStairs_sub(n):
            if n not in temp: 
                temp[n] = climbStairs_sub(n-1) + climbStairs_sub(n-2)
            return temp[n]
        return climbStairs_sub(n)
        
