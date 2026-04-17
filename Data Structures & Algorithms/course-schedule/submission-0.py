from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Build the graph and in-degree array
        graph = defaultdict(list)          # adjacency list: prereq -> courses that depend on it
        in_degree = [0] * numCourses       # in_degree[i] = number of prerequisites course i has

        for course, prereq in prerequisites:
            graph[prereq].append(course)   # prereq -> course
            in_degree[course] += 1         # course gains an incoming edge

        # Step 2: Initialize queue with courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        # Step 3: Process courses in BFS order
        processed = 0                       # counter for number of courses we can take

        while queue:
            current = queue.popleft()
            processed += 1                  # mark this course as "taken"

            # Step 4: Reduce in-degree of courses that depend on current
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1    # one prerequisite satisfied
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)  # now ready to take

        # Step 5: Check if all courses have been taken
        return processed == numCourses        # True if no cycles, False if some courses blocked
