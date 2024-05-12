#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])

        alantic = set()
        pacific = set()
        def dfs(row, col, prevHeight, oceanSet):
            if (row < 0 or col < 0) or (row >= n or col >= m) \
            or (heights[row][col] < prevHeight) \
            or ((row, col) in oceanSet):
                return

            oceanSet.add((row, col))

            for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                dfs(r, c, heights[row][col], oceanSet)


        for row in range(n):
            dfs(row, 0, heights[row][0], pacific)
            dfs(row, m - 1, heights[row][m - 1], alantic)

        for col in range(m):
            dfs(n - 1, col, heights[n - 1][col], alantic)
            dfs(0, col, heights[0][col], pacific)

        alantic.intersection_update(pacific)
        return list(alantic)

# @lc code=end

