class Solution:
    def lcs(self, s1, s2):
        # code here
        l1 = len(s1) + 1
        l2 = len(s2) + 1
        dp = [[-1] * l2 for _ in range(l1)]
        
        for i in range(l1):
            dp[i][0] = 0
        
        for j in range(l2):
            dp[0][j] = 0
        for i in range(1 , l1):
            for j in range(1 , l2):
                if s1[i-1] == s2[j-1]:
                    temp = 1 + dp[i-1][j-1]
                    dp[i][j] = temp
                
                else:
                    val1 = dp[i-1][j]
                    val2 = dp[i][j-1]
                    dp[i][j] = max(val1, val2)
        
        
        return dp[l1-1][l2-1]
        
        
        # def recurse(text1, text2, idx1, idx2):
        #     if idx1 >= len(text1) or idx2 >= len(text2):
        #         return 0
        #     if dp[idx1][idx2] != -1:
        #         return dp[idx1][idx2]

        #     if text1[idx1] == text2[idx2]:

        #         temp =  (1 + recurse(text1 , text2 , idx1 + 1, idx2 + 1))
        #         dp[idx1][idx2] = temp
        #         return temp

        #     elif text1[idx1] != text2[idx2]:
        #         val1 = recurse(text1, text2, idx1 + 1, idx2)
        #         val2 = recurse(text1, text2, idx1, idx2 + 1)

        #         temp = max(val1, val2)
        #         dp[idx1][idx2] = temp
        #         return temp

        # return (recurse(text1, text2, 0, 0))   