#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        
        for _ in range(n - 1):
            temp = one
            one += two
            two = temp

        return one
        
# @lc code=end
