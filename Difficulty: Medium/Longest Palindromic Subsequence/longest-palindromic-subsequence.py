class Solution:
    def longestPalinSubseq(self, s):
        # code here
        l1 = len(s) + 1
        l2 = len(s) + 1
        
        s1 = s
        s2 = s[::-1]
        
        dp = [[0] * l1 for _ in range(l2)]
        for i in range(1, l1):
            
            
            for j in range(1, l2):
                
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    
                else:
                    if dp[i-1][j] > dp[i][j-1]:
                        dp[i][j] = dp[i-1][j]
                        
                    else:
                        dp[i][j] = dp[i][j-1]
                        
        return dp[l1-1][l2-1]
                        