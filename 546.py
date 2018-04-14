class Solution:
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        len_boxes = len(boxes)
        temp_info = {}
        def removeBoxes_DP(i, j, k):
            if j < i:
                return 0
            if (i, j, k) not in temp_info:
                while i+1 <= j and boxes[i+1] == boxes[i]:
                    i, k = i + 1, k + 1
                temp = removeBoxes_DP(i+1, j, 0) + (k + 1)**2
                for m in range(i+1, j+1):
                    if boxes[m] == boxes[i]:
                        temp = max(removeBoxes_DP(i+1, m-1, 0) + removeBoxes_DP(m, j, k+1), temp)
                temp_info[(i, j, k)] = temp
            return temp_info[(i, j, k)]
        return removeBoxes_DP(0, len_boxes - 1, 0)
        
