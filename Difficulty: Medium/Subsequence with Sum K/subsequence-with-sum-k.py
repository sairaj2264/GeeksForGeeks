class Solution:
    def checkSubsequenceSum(self, arr, k):
        # code here
        min_sum = k
        dp = [[-1]* (min_sum + 1) for _ in range(len(arr) +1)]
        def recurse(i, summ):
            j = summ
            if summ == k:
                return True
                
            if i >= len(arr) or summ > k:
                return False
            
            if dp[i][j] != -1:
                return dp[i][j]
                
            ans1 = recurse(i+1, summ+ arr[i])
            if ans1 == True:
                dp[i][j] = True
                return True
            ans2 = recurse(i+1, summ)
            
            if ans2 == True:
                dp[i][j] = True
                return True
                
            dp[i][j] = False
            return False
        return recurse(0, 0)
            