#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        numIslands = 0
        def dfs(row, col):
            if row < 0 or row >= n or col < 0 or col >= m \
            or grid[row][col] == '0': return
            grid[row][col] = '0'

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)


        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1': 
                    dfs(i, j)
                    numIslands += 1

        return numIslands
                
# @lc code=end

