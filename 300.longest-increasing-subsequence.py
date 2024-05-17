#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        for i in range(1, n):
            # Select a value inside the dp[:i] if the value is less than current value then change our current dp value to that + 1
            filteredValues = [dp[j] for j in range(i) if nums[j] < nums[i]]
            if filteredValues:
                dp[i] = max(filteredValues) + 1


        return max(dp) + 1
# @lc code=end

