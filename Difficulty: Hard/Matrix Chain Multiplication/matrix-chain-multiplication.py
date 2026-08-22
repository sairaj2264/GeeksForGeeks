class Solution:
    def matrixMultiplication(self, arr):
        # code here
        
        start = 1
        end = len(arr) - 1
        dp = [[-1] * (len(arr) +2) for _ in range((len(arr) +2))]
        
        def recurse(arr, i,j):
            
            if i>=j:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            minn = float('inf')
            for k in range (i, j):
                
                temp1 = (recurse(arr, i,k) + recurse(arr, k+1, j)) + (arr[i-1] * arr[k] * arr[j])
                minn = min(minn, temp1)
            
            dp[i][j] = minn
            return minn
        
        return recurse(arr,start,end)
                
        