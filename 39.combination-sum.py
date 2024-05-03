#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Two ideas either you do a decision and choose to include when value already has been visited
        # Or can minus.

        candidates.sort(reverse=True)

        print(candidates)

        def backtrack(path, target):
            if target == 0:
                return path
            if target < 0:
                return
            for i in range(len(candidates)):
                backtrack(path + [candidates[i]], target - candidates[i])


        res = []
        backtrack(res, target)
        return res
        

            
        
# @lc code=end
