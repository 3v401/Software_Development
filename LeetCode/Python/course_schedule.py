# URL: https://leetcode.com/problems/course-schedule/description/

"""
False means there is a cycle
True means there is no cycle
We will work with graphs represented by adjacence lists, not Trees
"""

from collections import defaultdict
# defaultdict to autocreate lists as values

class Solution:
    def course_schedule(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        graph = defaultdict(list)
        # build adjacency list for graph
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # The graph is built, now use dfs to check for cycles
		# if dfs returns False → cycle found → course_schedule returns False

        # Create two sets to know trajectories already solved and under study
        visited = set()
        # path already solved (no need to study it again)
        visiting = set()
        # path under study

        def dfs(course: int) -> bool:

            if course in visiting:
                # if course is introduced again, there is a cycle
                return False
            
            if course in visited:
                # if course was already introduced in visited, no need to study it again
                return True
            
            visiting.add(course)
            # if this course is not in visiting/visited yet, add it to visiting

            # we are studying each course from numCourses
			# we must study the prereq from prerequisites here (child nodes)
            for prereq in graph[course]:
                # check the prerequisites on this course
                if not dfs(prereq): # if dfs(prereq)==False:
                    # if there is a cycle in the prereqs of the current course
                    return False
                
            visiting.remove(course)
            # we finished exploring all the requisites of this course
            visited.add(course)
            # we add this course to the safe set of courses
            # If we arrive to this point without triggering False
            # it means that the course is safe and there are no cycles
            
            return True
        
        for course in range(numCourses):
            # For each course in numCourses
            if not dfs(course):
                # if a cycle is found --> return False
                return False
        
        # if no cycles found throughout all the code
        return True
    

if __name__ == "__main__":

    sol = Solution()
    print(sol.course_schedule(2, [[1,0]]))
    print(sol.course_schedule(2, [[1,0],[0,1]]))