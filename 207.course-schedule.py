#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}

        for req in prerequisites:
            course, preq = req[0], req[1]
            if course not in graph: graph[course] = []
            graph[course].append(preq)

        visited = set()
        def dfs(current):
            if current in visited:
                print(current)
                return False

            visited.add(current)
            for neighbour in graph.get(current, []):
                if not dfs(neighbour): return False

            visited.remove(current)
            graph[current] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


# @lc code=end

