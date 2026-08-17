class Solution:
    def cutRod(self, price: list[int]) -> int:
        # code here
    
        n = len(price)
        price.insert(0,0)
        # print(price)
        maxx = 0
        maxx_idx = 0
        dp = [-1]*(n + 2) 
        def recurse( n):
            # print(n)
            if n <= 0:
                return 0
                
            # if idx > n:
            #     return float('-inf')
                
            if dp[n] != -1:
                return dp[n]
            # if dp[idx][n-idx] != -1:
            #     return dp[idx][n-idx]
            # val1 = price[idx] + recurse(price, idx, (n - idx))
            # val2 = recurse(price, idx + 1, n)
            # ans = max(val1, val2)
            # # print(ans)
            # dp[idx][n-idx] = ans
            # return ans
            
            maxx = 0
            for i in range(1 , n+1):
                temp = price[i]  + recurse( n - i)
                maxx = max(temp, maxx)
            dp[n] = maxx
            return maxx
                
            
            
        
        ans = recurse(n)
        # print(ans)
        return ans