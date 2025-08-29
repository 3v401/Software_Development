# URL: https://leetcode.com/problems/sliding-window-maximum/description/

from collections import deque

class Solution:
    def swm(self, nums: list[int], k: int) -> list[int]:

        dq = deque()
        # store indices of elements, decreasing order of values
        res: list[int] = []
        # answer of the program

        for i, num in enumerate(nums):

            if dq and dq[0] <= i-k:
                # i-k = -3,-2,-1,|0,1,2...
                # 1. If there are elements, and the biggest one is outside of our window
                dq.popleft()

            while dq and nums[dq[-1]] < num:
                # while there are elements and the latest dq num is < new biggest
                # 2  Maintain decreasing order (pop smaller elements from the back)
                dq.pop()

            dq.append(i)

            if i>=k-1:
                # 4.  if size of window ready, grab highest num
                res.append(nums[dq[0]])

        return res
    
if __name__ == '__main__':

    sol = Solution()
    print(sol.swm([1,3,-1,-3,5,3,6,7], 3))
    print(sol.swm([1],1))