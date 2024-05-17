#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Idea is to expand outwards.
        n = len(s)
        longestString = ('', 0)
        for i in range(n):
            # Odd case
            l = i
            r = i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > longestString[1]:
                    longestString = (s[l:r + 1], r - l + 1)
                l -= 1
                r += 1

            # Even case
            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > longestString[1]:
                    longestString = (s[l:r + 1], r - l + 1)
                l -= 1
                r += 1
        return longestString[0]

# @lc code=end

