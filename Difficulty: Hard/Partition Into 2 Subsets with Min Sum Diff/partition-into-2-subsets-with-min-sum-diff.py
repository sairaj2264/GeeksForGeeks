class Solution:
    def minDifference(self, arr: list[int]) -> int:
        # code here
        
        summ = 0
        
        for i in range(0 , len(arr)):
            summ += arr[i]
            
        target = summ//2
        dp = [[-1] * (summ + 1) for i in range(len(arr) + 1)]
        
        def recurse(arr, idx, target, summ):
            if summ == target:
                return True
            
            if idx >= len(arr) or summ > target:
                return False
            
            if dp[idx][summ] != -1:
                if dp[idx][summ] == 1:
                    return True
                return False
                
            ans = recurse(arr, idx + 1, target, summ + arr[idx])
            if ans == True:
                dp[idx][summ] = 1
                return True
            
            ans = recurse(arr, idx + 1, target, summ)
            if ans == True:
                dp[idx][summ] = 1
            else:
                dp[idx][summ] = 0
            return ans
            
        ans = 0
        
        for i in range(target , -1,-1):
            dp = [[-1] * (summ + 1) for i in range(len(arr) + 1)]
            if recurse(arr, 0, i, 0) == True:
                ans = i
                break
            
        
        return (summ - (2 *ans)) 