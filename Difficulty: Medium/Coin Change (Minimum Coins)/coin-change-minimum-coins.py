class Solution:
    def minCoins(self, coins: list[int], sum: int) -> int:
        # code here
        n = len(coins)
        
        dp = [[-1] * (len(coins) + 2)  for i in range(sum + 2)]
        
        
        def recurse(i, sum):
            
            if sum == 0:
                return 0
                
            if sum < 0:
                return float('inf')
                
            if i >= len(coins):
                return float('inf')
            
            if dp[sum][i] != -1:
                return dp[sum][i]
            val1 = 1 + recurse(i, sum - coins[i])
            val2 = recurse(i + 1, sum)
            temp = min(val1, val2)
            dp[sum][i] = temp
            return temp
            
            
        ans = (recurse(0, sum))
        if ans == float('inf'):
            return -1
            
        return ans