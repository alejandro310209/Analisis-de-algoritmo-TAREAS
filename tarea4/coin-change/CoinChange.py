class Solution:
    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for x in range(1, amount + 1):
            for coin in coins:
                if coin <= x:
                    dp[x] = min(dp[x], 1 + dp[x - coin])

        if dp[amount] == amount + 1:
            return -1

        return dp[amount]