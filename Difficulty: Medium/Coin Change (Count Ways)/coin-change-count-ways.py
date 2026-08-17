class Solution:
    def count(self, coins: list[int], sum: int) -> int:
        # code here
        n = len(coins)
        n+=2
        dp = [[-1] * n for _ in range(0, (sum + 2))]
        def recurse(i,summ):
            if summ == 0:
                return 1
                
            if summ < 0:
                return 0
            # print(coins)
            
            if i >= len(coins):
                return 0
            
            if dp[summ][i] != -1:
                return dp[summ][i]
            temp1 = recurse(i, summ - coins[i])
            temp2 = recurse(i + 1, summ)
            ans = temp1 + temp2
            dp[summ][i] = ans
            return ans
            
        return recurse(0,sum)