class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        r = len(image)
        c = len(image[0])
        org_color = image[sr][sc]
        if org_color == newColor:
            return image
        def dfs(sr_new, sc_new):
            if image[sr_new][sc_new] == org_color:
                image[sr_new][sc_new] = newColor
                if sr_new - 1 >= 0:
                    dfs(sr_new - 1, sc_new)
                if sr_new + 1 < r:
                    dfs(sr_new + 1, sc_new)
                if sc_new - 1 >= 0:
                    dfs(sr_new, sc_new - 1)
                if sc_new + 1 < c:
                    dfs(sr_new, sc_new + 1)
        dfs(sr, sc)
        return image
