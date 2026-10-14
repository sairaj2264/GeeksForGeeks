class Solution:
    def minCost(self, height: list[int]) -> int:
        # code here

        n = (len(height) -1)
        
        
        dp = [-1] * n
        def recurse(i,n):
            if i == n:
                return 0
                
            if dp[i] != -1:
                return dp[i]
            temp1 = 100000
            temp2 = 100000
            
            temp1 = (abs(height[i] - height[i+1]) + recurse(i + 1,n))
            
            if (i + 2) <= n:
                temp2 = (abs(height[i] - height[i + 2]) + recurse(i + 2,n))
            dp[i] = min(temp1, temp2)
            return dp[i]
        
        return recurse(0,n)
        
        # n = len(height)
        # if n == 1:
        #     return 0
            
        # if n == 2:
        #     return abs(height[0] - height[1])
        
        # answer = 0
        # # current = height[0]
        # dp = [-1] * n
        # dp[0] = height[0]
        # dp[1] = abs(height[0] - height[1])
        

        # def jumper(dp, index, n, ans):
            
        #     if index == n:
        #         return ans
            
        #     if dp[index + 1] == -1:
                
        #         dp[index + 1] = jumper(dp, index + 1, n, ans)
            
        #     if dp[index + 2] == -1:
        #         dp[index + 2] = jumper(dp, index + 2, n, ans)
                
        #     ans1 = abs(dp[index] - dp[index + 1])
        #     ans2 = abs(dp[index] - dp[index + 2])
        #     ans = min(ans1, ans2)
        #     return ans
        # index = 0
        # ans = 0
        
        # answer = jumper(dp, index, n, ans)
        # return answer
            
        # i = 0
        # while(i < (n-1)):
        #     current = height[i]
        #     temp1 = abs(current - height[i + 1])
        #     temp2 = float('inf')
        #     if (i + 2) < n:
        #         temp2 = abs(current - height[i + 2])
            
        #     if temp1 < temp2:
        #         answer += temp1
        #         i+=1
        #     else:
        #         answer += temp2
        #         i+=2
            
        # return answer
            