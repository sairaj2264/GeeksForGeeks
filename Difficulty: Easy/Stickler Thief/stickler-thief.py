class Solution:  
    def findMaxSum(self, arr):
        # code here
        
        dp = [-1] * (len(arr) + 1)
        def recurse(i):
            if i >= len(arr):
                return 0
            
            if dp[i] != -1:
                return dp[i]
                
            temp1 = (arr[i] + recurse(i + 2))
            temp2 = recurse(i+1)
            dp[i] = max(temp1, temp2)
            return dp[i]
            
        return recurse(0)
            
            