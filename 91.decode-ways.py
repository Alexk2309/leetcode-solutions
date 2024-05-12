#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0': return 0

        n2, n1 = 1, 1
        for i in range(2, len(s) + 1):
            currN = 0
            if s[i - 1] != '0':
                currN += n1
    
            doubleDigit = s[i - 2: i]
            if 10 <= int(doubleDigit) <= 26:
                currN += n2
    
            n2, n1 = n1, currN

        return n1

        
# @lc code=end

