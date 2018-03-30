class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return None
        if digits[-1] == 9:
            digits[-1] = 0
            if not digits[:-1]:
                digits = [1] +  digits
                return digits
            digits[:-1] = self.plusOne(digits[:-1])
        else:
            digits[-1] += 1 
        return digits
            