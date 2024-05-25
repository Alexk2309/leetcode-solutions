#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m: return False

        baseCharacters = {}
        comparisonDict = {}
        for i in range(n):
            baseCharacters[s1[i]] = baseCharacters.get(s1[i], 0) + 1

            if i != n - 1:
                comparisonDict[s2[i]] = comparisonDict.get(s2[i], 0) + 1
        windowSize = n - 1

        l = 0
        for r in range(windowSize, m):
            comparisonDict[s2[r]] = comparisonDict.get(s2[r], 0) + 1
            if comparisonDict == baseCharacters: return True
            comparisonDict[s2[l]] -= 1
            if comparisonDict[s2[l]] == 0:
                del comparisonDict[s2[l]]
            l += 1

        return False
# @lc code=end

