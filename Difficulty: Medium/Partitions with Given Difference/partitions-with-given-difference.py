class Solution:
    def countPartitions(self, arr, diff):
        # code here
        total = 0
        
        for i in range(0 , len(arr)):
            total+= arr[i]
            
        target = (total + diff)
        # print(target)
        # dp = [[-1]*target for i in range(len(arr))]
        nums = []
        dp = [[-1] * (2 * target) for _ in range(len(arr))]

        def recurse(arr, target, i, summ):
            if i >= len(arr):
                if (2 * summ) == target:
                    return 1
                return 0
            
            if (2*summ) > target or i >= len(arr):
                return 0
                
            if dp[i][summ] != -1:
                return dp[i][summ]
            ans1 = recurse(arr, target, i + 1, summ + arr[i])
            ans2 = recurse(arr, target, i + 1, summ)
            dp[i][summ] = ans1 + ans2
            return (ans1 + ans2)
                

        
        return recurse(arr, target, 0, 0)
        