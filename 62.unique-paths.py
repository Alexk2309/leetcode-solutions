#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n: return 0
            if (x, y) in memo: return memo[(x, y)]
            if x == m - 1 and y == n - 1: 
                return 1

            res = dfs(x + 1, y) + dfs(x, y + 1)
            memo[(x, y)] = res
            
            return res
        
        return dfs(0, 0)





        
# @lc code=end

