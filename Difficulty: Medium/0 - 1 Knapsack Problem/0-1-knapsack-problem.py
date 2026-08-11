class Solution:
    def knapsack(self, W: int, val: list[int], wt: list[int]) -> int:

        dp = [0] * (W + 1)

        for n in range(len(wt)):
            for w in range(W, wt[n] - 1, -1):
                dp[w] = max(dp[w], val[n] + dp[w - wt[n]])

        return dp[W]