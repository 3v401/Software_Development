# URL: https://leetcode.com/problems/rotting-oranges/description/

"""
A deque stands for Double-Ended Queue.
It is a data structure that allows adding
and removing elements from both ends efficiently.
Unlike regular queues, which are typically
operated on using FIFO (First In, First Out)
principles, a deque supports both FIFO and LIFO.
"""

# BFS is used properly with a queue and time tracking.

from collections import deque

def bfs(grid: list[list[int]], queue, fresh: int) -> int:

  rows, cols = len(grid), len(grid[0])
  directions = [(1,0), (-1,0), (0,1), (0,-1)]
  maxtime = 0

  while queue:
    # while root oranges to activate
    r, c, time = queue.popleft()
    # grab coordinates and time from rooted oranges
    maxtime = max(maxtime, time)
    for dr, dc in directions:
      nr, nc = r+dr, c+dc
      # coordinates of action

      if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
        # if inside of the grid a fresh orange is found
        grid[nr][nc] = 2
        queue.append((nr, nc, time+1))
        fresh -=1
        # infect it + save coordinates and time + reduce fresh oranges

  return maxtime if fresh == 0 else -1


def rotten_oranges(grid: list[list[int]]) -> int:

    rows, cols = len(grid), len(grid[0])
    fresh = 0
    queue = deque()

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
                # count number of rotten oranges at initial time with its coordinates
            elif grid[r][c] == 1:
                fresh +=1
                # count number of fresh oranges at initial time

    return bfs(grid, queue, fresh)

if __name__ == "__main__":
   
   print(rotten_oranges([[2,1,1],[1,1,0],[0,1,1]]))
   print(rotten_oranges([[2,1,1],[0,1,1],[1,0,1]]))
   print(rotten_oranges([[0,2]]))