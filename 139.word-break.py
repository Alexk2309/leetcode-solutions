#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Memo Solution

        # def getNewStr(ogStr, substring):
        #     if ogStr.startswith(substring):
        #         return ogStr[len(substring):]
        #     return ogStr

        # memo = {}
        # def breakDown(currStr):
        #     if currStr == '': return True
        #     if currStr in memo: return memo[currStr]
        #     res = False
        #     for substring in wordDict:
        #         newString = getNewStr(currStr, substring)
        #         if newString == currStr: continue
        #         res = res or breakDown(newString)
        #         if res: break

        #     memo[currStr] = res
        #     return res

        # return breakDown(s)

        # Tabulation Solution

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        maxStrLen = max(map(len, wordDict))

        for i in range(0, n + 1):
            for j in range(i, min(i + maxStrLen, n + 1)):
                try:
                    wordIndex = wordDict.index(s[i:j + 1])
                    word = wordDict[wordIndex]
                    if dp[j - len(word) + 1]:
                        dp[j + 1] = True
                except:
                    pass

        return dp[n]

# @lc code=end

