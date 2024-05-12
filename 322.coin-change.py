#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Memo Solution

        # memo = {}
        # def findMin(amount):
        #     if amount < 0: return float('inf')
        #     if amount == 0: return 0
        #     if amount in memo: return memo[amount]

        #     res = float('inf')
        #     for coin in coins:
        #         res = min(res, findMin(amount - coin) + 1)

        #     memo[amount] = res

        #     return res

        # res = findMin(amount)
        # return res if res != float('inf') else - 1

        # Tabulation

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

# @lc code=end

