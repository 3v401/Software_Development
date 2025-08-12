# URL: https://leetcode.com/problems/clone-graph/

# The code to build the graph from adjList is handled in LeetCode (or a helper).
# We focus on what should be cloneGraph(node) function

"""
We will define two classes:

Node: Represents single node in the graph with .val and .neighbors
Solution: Groups the algorithm 'cloneGraph' with the other functions provided by Leetcode

A class is a blueprint for creating objects in python (data + behavior)
"""

class Node:
    def __init__(self, val = 0, neighbors = None):

        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:

    def clonegraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            # edge case
            return None
        
        visited = {}
        # dictionary to avoid repetitions (looped graphs)

        def dfs(current_node: 'Node') -> 'Node':

            if current_node in visited:
                # return already cloned node
                return visited[current_node]
            
            copy = Node(current_node.val)
            # copy the value of the current Node object
            visited[current_node] = copy
            # store the visited node in the dictionary

            for nei in current_node.neighbors:
                # copy each neighbors of the current Node object
                # dfs ensures we also recursively clone all their neighbors
                # by starting at the root, we clone the entire connected graph until the end

                copy.neighbors.append(dfs(nei))

            return copy
            
        return dfs(node)
    


# TO DO:

# Create: graph_to_adjlist(cloned_graph)
# Create: adjlist_to_graph(adjlist)