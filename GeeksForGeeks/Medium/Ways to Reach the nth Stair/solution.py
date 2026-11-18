class Solution:
    def countWays(self, n: int) -> int:
        # code here
        
        
        dp = [-1] * (n + 1)
        
        # def recurse(n):
        #     if n == 0:
        #         return 0
            
        #     elif n == 1:
        #         return 1
            
        #     elif n == 2:
        #         return 2
            
        #     elif n == 3:
        #         return 3
                
        #     else:
        #         if dp[n] != -1:
        #             return dp[n]
        #         else:
        #             dp[n] =  (recurse(n-1) + recurse(n - 2))
        #             return dp[n]
                    
        
        # answer = recurse(n)
        
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i - 2]
            
        return dp[n]
            