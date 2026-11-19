class Solution:
    def maximumPoints(self, mat):
        # code here
        
        dp = [[-1] * (len(mat[0]) + 2) for _ in range(len(mat) + 2)]
        def recurse(x,ji):
            if x >= len(mat):
                return 0
            if dp[x][ji] != -1:
                return dp[x][ji]
                
            temp = 0
            for j in range(0 , len(mat[0])):
                if j != ji:
                    temp1 = mat[x][j] + recurse(x+1, j)
                    temp = max(temp1, temp)
                
                            
            dp[x][ji] = temp           
            return temp
        
        return recurse(0,-1)
                