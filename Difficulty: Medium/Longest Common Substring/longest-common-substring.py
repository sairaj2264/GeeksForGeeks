class Solution:
    def longCommSubstr(self, s1, s2):
        # code here
        a = max(len(s1), len(s2))
        maxx = 0
        
        dp = [[0]* (len(s2) + 1) for _ in range(len(s1) + 1)]
        
        
        for i in range(0 , len(s1) + 1):
            dp[i][0] = 0
            
        for i in range(0 , len(s2) + 1):
            dp[0][i] = 0
            
        for i in range(1 , len(s1) + 1):
            
            for j in range(1 , len(s2) + 1):
                
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = (1 + dp[i-1][j-1])
                    maxx = max(dp[i][j], maxx)
                else:  
                    dp[i][j] = 0
                
        # print(dp)
        return maxx
        
        # print(dp)
        # uzvnzr
        
        # def recurse(idx1, idx2, count):
        #     nonlocal maxx
        #     if idx1 >= len(s1) or idx2 >= len(s2):
        #         return count
            
        #     if dp[idx1][idx2] !=-1:
        #         return dp[idx1][idx2]
                
        #     match_count = count
        #     if s1[idx1] == s2[idx2]:
        #         match_count = recurse(idx1 + 1, idx2 + 1, count + 1)

            
        #     val1 = recurse(idx1 + 1, idx2, 0)
        #     val2 = recurse(idx1, idx2 + 1, 0)
            
            
                
        #     temp = max(val1, val2, match_count)
        #     dp[idx1][idx2] = temp
        #     maxx = max(maxx, temp)
        #     return temp
                
        # a = recurse(0, 0, 0)
        # return maxx