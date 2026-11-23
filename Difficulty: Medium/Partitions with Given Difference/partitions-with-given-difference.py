class Solution:
    def countPartitions(self, arr, diff):
        # code here
        total = sum(arr)
        
        dp = [[-1] * (total + 2) for _ in range(len(arr)+2)]
        def recurse(i,summ):
            if i >= len(arr):
                if (summ - (total - summ)) == diff:
                    return 1
                else:
                    return 0
            if dp[i][summ] != -1:
                return dp[i][summ]
                
                
            dp[i][summ] = ( recurse(i+1, summ+arr[i]) + recurse(i+1, summ))
            return dp[i][summ]
        
        return recurse(0,0)
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # total = 0
        
        # for i in range(0 , len(arr)):
        #     total+= arr[i]
            
        # target = (total + diff)
        # # print(target)
        # # dp = [[-1]*target for i in range(len(arr))]
        # nums = []
        # dp = [[-1] * (2 * target) for _ in range(len(arr))]

        # def recurse(arr, target, i, summ):
        #     if i >= len(arr):
        #         if (2 * summ) == target:
        #             return 1
        #         return 0
            
        #     if (2*summ) > target or i >= len(arr):
        #         return 0
                
        #     if dp[i][summ] != -1:
        #         return dp[i][summ]
        #     ans1 = recurse(arr, target, i + 1, summ + arr[i])
        #     ans2 = recurse(arr, target, i + 1, summ)
        #     dp[i][summ] = ans1 + ans2
        #     return (ans1 + ans2)
                

        
        # return recurse(arr, target, 0, 0)
        