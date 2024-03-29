#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        index = -1
        while l <= r:
            mid = (r + l) // 2
            print(mid)
            if target == nums[mid]: return mid
            # [4,5,6,7,0,1,2]
            #  l     m   t  r
            if target < nums[mid]:
                # So the target is smaller than mid
                # Since the middle number is greater than r, and the target is less than l
                if nums[mid] > nums[r] and target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # Since the middle number is less than the number on the right and target is greater than the number right
                # This means there is going to be a wrap around for a number bigger than r and greater r
                if nums[mid] < nums[r] and target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return index
# @lc code=end

