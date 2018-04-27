class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        position = []
        for i, e in enumerate(S):
            if e == C:
                position.append(i)
        distance_list = []
        for i in range(len(S)):
            distance_list.append(bin_search(0, len(position) - 1, position, i))
        return distance_list
    
def bin_search(start_pos, end_pos, position, i):
    if i <= position[start_pos]:
        return(position[start_pos] - i)
    elif i >= position[end_pos]:
        return(i - position[end_pos])
    if end_pos - start_pos == 1:
        return(min(position[end_pos] - i, i - position[start_pos]))
    while end_pos - start_pos >= 2:
        temp = int((start_pos + end_pos)/2)
        if i > position[temp]:
            new_start_pos = temp
            new_end_pos = end_pos
        else:
            new_start_pos = start_pos
            new_end_pos = temp
        return bin_search(new_start_pos, new_end_pos, position, i)

def test_run():
    a = Solution()
    b = a.shortestToChar('loveleetcode','e')
    print(b)
    
if __name__ == "__main__":
    test_run()
