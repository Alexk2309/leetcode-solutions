#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        visited = set()
        memo = {}
        def scout(index):
            if index >= n or index in visited: return 0

            if index in memo: return memo[index]

            visited.add(index)
            rob_current = nums[index] + scout(index + 2)
            skip_current = scout(index + 1)
            res = max(rob_current, skip_current)

            visited.remove(index)
            memo[index] = res

            return res


        return scout(0)

# @lc code=end

