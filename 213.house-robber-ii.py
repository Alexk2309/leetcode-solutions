#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob1(nums):
            house1, house2 = 0, 0
            for value in nums:
                temp = max(house1 + value, house2)
                house1 = house2
                house2 = temp

            return house2

        return max(nums[0],rob1(nums[:-1]), rob1(nums[1:]))


# @lc code=end

