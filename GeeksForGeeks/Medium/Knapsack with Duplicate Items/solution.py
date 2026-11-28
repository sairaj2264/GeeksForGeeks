class Solution:
    def knapSack(self, val, wt, capacity):
        # code here
        
        dp = [[-1] * (capacity +2) for _ in range(len(val))]
        def recurse(i, capacity):
            
            if capacity == 0:
                return 0
            
            if capacity < 0:
                return -1000000
                
            if i>= len(val):
                return 0
            
            if dp[i][capacity] != -1:
                return dp[i][capacity]
                
            ans1 =  recurse(i, capacity - wt[i])
            if ans1 != -1000000:
                ans1 += val[i]
            ans2 = recurse(i+1, capacity)
            dp[i][capacity] = max(ans1, ans2)
            return dp[i][capacity]
            
        return recurse(0,capacity)