
from collections import defaultdict
from queue import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0]  * numCourses
        for courses, prereq in prerequisites:
            graph[prereq].append(courses)
            indegree[courses] += 1
        queue = deque()
        for courses in range(numCourses):
            if indegree[courses] == 0:
                queue.append(courses)
        process = 0
        while queue:
            current = queue.popleft()
            process += 1
            for nei in graph[current]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        if process == numCourses:
            return True
        return False
Solution = Solution()
print(Solution.canFinish(2, [[1,0]]))