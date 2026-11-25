class Solution:
    def totalWays(self, arr: list[int], target: int) -> int:
        # code here
        
        dp = [[-100000] * 1002 for _ in range(len(arr) + 2) ]
        
        def recurse(i, summ):
            
            if i >= len(arr) and summ == target:
                return 1
            
            elif i >= len(arr):
                return 0
                    
            if dp[i][summ] != -100000:
                return dp[i][summ]
            symbol_1 = recurse(i+1, summ + arr[i])
            symbol_2 = recurse(i+1, summ - arr[i])
            dp[i][summ] = (symbol_1 + symbol_2)
            return dp[i][summ]
        
        return recurse(0, 0)
                
            