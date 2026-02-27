from typing import List, Optional

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Approach: Depth-First Search (DFS) with graph traversal.
        Time Complexity: O(n + m), where n is the number of courses and m is the number of prerequisites.
        Space Complexity: O(n), where n is the number of courses.
        """
        # Create an adjacency list representation of the graph
        graph = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        # Initialize a visited set to keep track of visited courses
        visited = set()

        # Define a recursive DFS function
        def dfs(course):
            # If the course is already in the visited set, return False (cycle detected)
            if course in visited:
                return False

            # Mark the course as visited
            visited.add(course)

            # Iterate over the prerequisites of the current course
            for prerequisite in graph[course]:
                # If the prerequisite has not been visited, recursively call dfs on it
                if not dfs(prerequisite):
                    return False

            # If all prerequisites have been visited, return True
            return True

        # Iterate over all courses and perform DFS
        for course in range(numCourses):
            # If the course has not been visited, call dfs on it
            if course not in visited:
                if not dfs(course):
                    return False

        # If no cycles are detected, return True
        return True

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.canFinish(2, [[1,0]]))  # Expected: True
    print(s.canFinish(2, [[1,0],[0,1]]))  # Expected: False