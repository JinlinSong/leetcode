class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        s_dic = {}
        for e in cpdomains:
            pair = e.split(' ')
            count = int(pair[0])
            s = pair[1].split('.')
            temp_len = len(s)
            while temp_len >= 1:
                s_temp = '.'.join(s[-temp_len:])
                if s_temp in s_dic:
                    s_dic[s_temp] = int(s_dic[s_temp]) + count
                else:
                    s_dic[s_temp] = count
                temp_len -= 1
        return [str(s_dic[i]) + ' ' +  i for i in s_dic]
