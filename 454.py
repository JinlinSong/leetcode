class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dic_1 = {}
        for a in A:
            for b in B:
                if a + b in dic_1:
                    dic_1[a+b] += 1
                else:
                    dic_1[a+b] = 1
        count = 0
        for c in C:
            for d in D:
                if - c - d in dic_1:
                    count += dic_1[- c - d]
        return count
