class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        if not paragraph:
            return ''
        import re
        paragraph = paragraph.lower() + ' '
        paragraph = re.sub("[!?',;.]",'',paragraph)
        paragraph = re.sub("[ ]+",' ',paragraph)
        for e in banned:
            paragraph = paragraph.replace(e+' ','')
        paragraph = re.sub("[ ]+",' ',paragraph).strip().split(' ')
        
        ans = paragraph[0]
        numbers = 1
        for i in range(0, len(paragraph)):
            if paragraph.count(paragraph[i]) > numbers:
                ans = paragraph[i]
                numbers = paragraph.count(paragraph[i])
        return ans
