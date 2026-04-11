from typing import List, Optional
from collections import defaultdict, deque

class Solution:
    def isConflict(self, course1: str, course2: str) -> bool:
        """
        Check if two courses conflict.
        
        Args:
            course1 (str): The first course.
            course2 (str): The second course.
        
        Returns:
            bool: True if the courses conflict, False otherwise.
        """
        # For simplicity, assume that we have a dictionary with all possible courses
        # and their corresponding conflicts. In a real-world scenario, this would be 
        # retrieved from some database or file.
        conflicts = {
            "A": ["B", "D"],
            "B": ["C"],
            "C": [],
            "D": []
        }
        
        return course1 in conflicts[course2] or course2 in conflicts[course1]

    def addConflict(self, course1: str, course2: str) -> None:
        """
        Add a conflict between two courses.
        
        Args:
            course1 (str): The first course.
            course2 (str): The second course.
        """
        # For simplicity, assume that we have a dictionary with all possible courses
        # and their corresponding conflicts. In a real-world scenario, this would be 
        # retrieved from some database or file.
        conflicts = {
            "A": ["B", "D"],
            "B": ["C"],
            "C": [],
            "D": []
        }
        
        if course1 not in conflicts:
            conflicts[course1] = []
        
        if course2 not in conflicts:
            conflicts[course2] = []
        
        conflicts[course1].append(course2)
        conflicts[course2].append(course1)

    def checkSchedule(self, courses: List[str]) -> bool:
        """
        Check if a schedule is valid.
        
        Args:
            courses (List[str]): The list of courses.
        
        Returns:
            bool: True if the schedule is valid, False otherwise.
        """
        # Create a graph with all possible courses as nodes
        graph = defaultdict(list)
        in_degree = {course: 0 for course in set(courses)}
        
        # Add edges to the graph based on conflicts
        for i in range(len(courses)):
            for j in range(i + 1, len(courses)):
                if self.isConflict(courses[i], courses[j]):
                    graph[courses[i]].append(courses[j])
                    in_degree[courses[j]] += 1
        
        # Initialize a queue with all nodes that have an in-degree of 0
        queue = deque([course for course in in_degree if in_degree[course] == 0])
        
        # Perform topological sorting
        while queue:
            course = queue.popleft()
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If there are still nodes with an in-degree greater than 0, then the schedule is not valid
        return all(in_degree[course] == 0 for course in in_degree)

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.checkSchedule(["A", "B", "C"]))  # Expected: False
    print(s.checkSchedule(["A", "B", "D"]))  # Expected: True