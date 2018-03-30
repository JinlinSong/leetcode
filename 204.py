class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = n - 1
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        import math
        temp = int(math.floor(math.sqrt(n)))
        list_temp = set(range(2,n+1))
        for i in range(2, temp+1):
            if i not in list_temp:
                continue
            j = 2
            while True:
                potential_v = i*j
                if potential_v in list_temp:
                    list_temp.remove(potential_v)
                if potential_v > n:
                    break
                j += 1
        return len(list_temp)