# URL: https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/

"""
This algorithm works for every point.
Does outwards/inwards from every inserted point in last line.
"""

class Solution:
    def reorder_route(self, n: int, connections: list[list[int]]) -> int:

        graph = [[] for _ in range(n)]
        # adjacency list where each edge has a "flag" telling if it needs flipping
        for a, b in connections:
            graph[a].append((b,1))
            # if we move from a to b, it goes away from 0 --> needs flip
            graph[b].append((a,0))
            # good way b->a goes inwards
        # we will use this adjacency list with root "0", that's why inwards=good outwards=bad


        visited = [False] *n

        def dfs(u: int) -> int:
            # takes node label and returns flips (direction changes)
            visited[u] = True
            flips = 0
            for v, needs_flip in graph[u]:
                if not visited[v]:
                    # if v was not visited yet
                    flips += needs_flip
                    # add flip if needed
                    flips += dfs(v)
                    # call neighbor v and ad its result

            return flips
        
        # call dfs from - to check outwards how many flips are returned by dfs
        return dfs(0)
    
if __name__ == "__main__":

    sol = Solution()
    print(sol.reorder_route(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))