#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n - 1):
            amount = nums[i]
            if i > 0 and nums[i] == nums[i - 1]: continue
            if nums[i] > 0: break

            l, r = i + 1, n - 1
            while l < r:
                target = amount + nums[l] + nums[r]
                if target > 0:
                    r -= 1
                elif target < 0:
                    l += 1
                else:
                    res.append([amount, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
# @lc code=end

