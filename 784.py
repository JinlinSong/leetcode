class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ans = []
        def dfs(S,i,n):
            if i == n:
                ans.append(''.join(S))
                return
            dfs(S,i+1,n)
            if S[i].isalpha():
                S[i] = chr(ord(S[i])^(1<<5))
                dfs(S,i+1,n)
        dfs(list(S),0,len(S))
        return ans
 '''     
 class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ans = ['']
        for e in S:
            if e.isalpha():
                ans = [temp + e for e in [e, chr(ord(e)^(1<<5))] for temp in ans]
            else:
                ans = [temp + e for temp in ans]
        return ans
''' 
