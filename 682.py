class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        scores = []
        for e in ops:
            if e  == 'C':
                scores.pop()
                continue
            scores.append(e)
        total = 0
        for i, e in enumerate(scores):
            if e == 'D':
                scores[i] = 2*int(scores[i-1])
            if e == '+':
                scores[i] = int(scores[i-1]) + int(scores[i-2])
            total = total + int(scores[i])
        return total
