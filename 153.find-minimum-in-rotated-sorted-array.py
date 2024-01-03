#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        #[4,5,6,7,0,1,2]
        #l      m

        # Pick the right side because, the middle should always be less than the right side in normal binary search.
        # If nums[mid] <= nums[r], this means that the binary array is correct.
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]

# @lc code=end

