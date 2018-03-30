class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        i = 0
        countAndSay_list = ['1']
        while i < n-1:
            countAndSay_list.append(self.Count(countAndSay_list[i]))
            i += 1
        return countAndSay_list[-1]
    def Count(self, n):
        if not n:
            return ''
        result = ''
        n = n + 'E'
        before = n[0]
        temp = 1
        for i in range(1,len(n)):
            if n[i] == before:
                temp += 1
            else:
                result = result + str(temp) + before
                before = n[i]
                temp = 1
        return result