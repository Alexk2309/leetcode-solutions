#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        chars = []
        longestSubStr = 0
        for r in range(len(s)):
            while s[r] in chars:
                chars.pop(0)
                l += 1

            chars.append(s[r])
            longestSubStr = max(longestSubStr, len(chars))
            r += 1

        return longestSubStr

# @lc code=end

