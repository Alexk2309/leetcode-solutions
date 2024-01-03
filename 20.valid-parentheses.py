#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        bracMap = {'}': '{', ')': '(', ']': '[' }

        stack = []
        for bracket in s:
            if bracket not in bracMap.keys():
                stack.append(bracket)
                continue
            if not stack or stack[-1] != bracMap[bracket]:
                return False

            stack.pop()

        return not stack

# @lc code=end

