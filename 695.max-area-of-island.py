#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def dfs(row, col):
            if row < 0 or row >= n \
            or col < 0 or col >= m \
                or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            res = 1
            for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                res += dfs(r, c)

            return res

        greatest = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    greatest = max(greatest, dfs(i, j))

        return greatest

# @lc code=end
