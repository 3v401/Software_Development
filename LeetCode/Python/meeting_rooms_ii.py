# URL: https://neetcode.io/problems/meeting-schedule-ii
# https://leetcode.com/problems/meeting-rooms-ii/description/

'''In this example days = maxrooms + 1'''

import heapq

class Solution:
    def mrii(self, intervals: list[tuple[int, int]]) -> int:
        if not intervals:
            # edge case
            return 0
        
        intervals.sort(key = lambda x: x[0])
        # Sort meeting times
        ends = []
        # min-heap to track meeting end times
        maxrooms = 0
        for start, end in intervals:
            # For each meeting
            while ends and ends[0] <= start:
                # Free up rooms for meetings that have ended
                heapq.heappop(ends)
                # remove the earliest ending meeting (ending[0])

            heapq.heappush(ends, end)
            maxrooms = max(maxrooms, len(ends))
        return maxrooms
    
if __name__ == '__main__':

    sol = Solution()
    print(sol.mrii([(0,40),(5,10),(15,20)]))
    print(sol.mrii([(4,9)]))