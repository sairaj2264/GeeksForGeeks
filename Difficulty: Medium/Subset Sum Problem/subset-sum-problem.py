class Solution:
    def isSubsetSum(self, arr: list[int], sum: int) -> bool:
        # code here
        dp = [[-1] * (sum + 2) for i in range(len(arr) + 2)]
        
        # print(dp)
        def recurse(arr, target, idx):
            if target < 0:
                return False
            if target == 0:
                return True
                
            if idx >= len(arr):
                dp[idx][target] = 0
                return False
                
            if dp[idx][target] != -1:
                if dp[idx][target] == 1:
                    return True
                return False

            ans1 =  recurse(arr, target - arr[idx], idx + 1)
            if ans1 == True:
                dp[idx][target] = 1
                return True
                
                
            else:
                dp[idx][target] = 0
                ans2 = recurse(arr, target, idx + 1)
            
                if ans2 == True:
                    dp[idx][target] = 1
                    return True
                    dp[idx][target] = 0
                
 
            dp[idx][target] = 0
            return False
                
        
        return(recurse(arr, sum, 0))
            
            
                
            
        