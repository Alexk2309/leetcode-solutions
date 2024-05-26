#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        outerL = 0
        outerR = m - 1
        while outerL <= outerR:
            outerMid = outerL + (outerR - outerL) // 2
            startCol, endCol = matrix[outerMid][0], matrix[outerMid][n - 1]
            if startCol <= target <= endCol:
                innerL = 0
                innerR = n - 1
                while innerL <= innerR:
                    innerMid = innerL + (innerR - innerL) // 2
                    number = matrix[outerMid][innerMid]
                    if number < target:
                        innerL = innerMid + 1
                    elif number > target:
                        innerR = innerMid - 1
                    else:
                        return True
                break
            else:
                if target < startCol:
                    outerR = outerMid - 1
                else:
                    outerL = outerMid + 1

        return False
# @lc code=end

