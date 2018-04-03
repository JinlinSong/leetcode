class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        import collections
        count = collections.Counter(words)
        candidates = list(count.keys())
        candidates.sort(key = lambda w: (-count[w], w))
        return candidates[:k]
