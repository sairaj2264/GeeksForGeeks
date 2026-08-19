class Solution:
    def minSuperSeq(self, s1, s2):
        # code here
        l1 = len(s1) + 1
        l2 = len(s2) + 1

        dp = [[0]* l2 for i in range(l1)]

        # print(dp)

        for i in range(1, l1):

            for j in range(1 , l2):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        temp = dp[l1-1][l2-1]
        
        total = l1 + l2 - 2
        
        ans = total - temp
        
        return ans