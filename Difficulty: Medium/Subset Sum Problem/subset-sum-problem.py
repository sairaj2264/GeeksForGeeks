class Solution:
    def isSubsetSum(self, arr: list[int], sum: int) -> bool:
        # code here
        n = len(arr)
        dp = [[-1] * (sum + 1) for _ in range(len(arr) + 1)]
        def recurse(i,summ):
            if i >= n and summ != 0:
                return False
            
            elif summ == 0:
                return True
            
            elif summ < 0:
                return False
            
            if dp[i][summ] != -1:
                return dp[i][summ]
            ans1 = recurse(i+1, summ)
            ans2 = recurse(i+1, summ - arr[i])
            
            if ans1 == True or ans2 == True:
                dp[i][summ] = True
                return True
            
            dp[i][summ] = False
            return False
            
        
        return recurse(0, sum)
                
            