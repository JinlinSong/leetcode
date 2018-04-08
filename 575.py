class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        types = len(set(candies))
        numbers = len(candies)
        return min(types, int(numbers/2))
