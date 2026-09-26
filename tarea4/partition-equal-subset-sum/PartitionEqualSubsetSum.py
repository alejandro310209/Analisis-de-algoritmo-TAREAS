class Solution:
    def canPartition(self, nums):
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for w in range(target, num - 1, -1):
                dp[w] = dp[w] or dp[w - num]

        return dp[target]