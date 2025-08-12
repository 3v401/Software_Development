# URL: https://leetcode.com/problems/pacific-atlantic-water-flow/description/

class Solution:
    def pawf(self, heights: list[list[int]]) -> list[list[int]]:

        if not heights:
            # edge case
            return []
        
        atlantic = set()
        pacific = set()
        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, area, prev_height):

            # we use dfs to move inwards from grid coast to intersection pacific+atlantic

            if (
                r<0 or c<0 or                   # out up or left
                r>=rows or c>=cols or           # out down or right
                (r,c) in area or                # [r][c] already visited
                heights[r][c] < prev_height    # current height < prev height (yes, we are moving inwards)
            ):
                # if any of these conditions are met, stop dfs
                return
            
            # if none of these conditions are met, continue
            
            area.add((r,c))
            # add the current point to visited area

            dfs(r, c+1, area, heights[r][c])            # right
            dfs(r, c-1, area, heights[r][c])            # left
            dfs(r-1, c, area, heights[r][c])            # up
            dfs(r+1, c, area, heights[r][c])            # down

        # now call dfs on the borders of each area
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])               # leftmost
            dfs(r, cols-1, atlantic, heights[r][cols-1])    # rightmost
        
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])               # upmost
            dfs(rows-1, c, atlantic, heights[rows-1][c])    # bottom

        return [[r,c] for (r,c) in pacific & atlantic]
    
if __name__ == "__main__":

    sol = Solution()
    print(sol.pawf([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
    print(sol.pawf([[1]]))