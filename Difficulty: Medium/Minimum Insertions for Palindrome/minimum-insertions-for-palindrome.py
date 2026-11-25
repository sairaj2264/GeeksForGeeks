class Solution:
    def findMinInsertions(self, s):
        # code here
        dp = [[-1] * (len(s)+1) for _ in range(len(s)+1)]
        def recurse(i,j):
            
            if i > j:
                return 0
                
            if dp[i][j] != -1:
                return dp[i][j]
                
            if s[i] == s[j]:
                if i != j:
                    dp[i][j] = (2 + recurse(i+1, j-1))
                    return dp[i][j]
                else:
                    dp[i][j] = (1 + recurse(i+1, j-1))
                    return dp[i][j]
            palin1 = recurse(i+1, j)
            palin2 = recurse(i, j-1)
            dp[i][j] = max(palin1, palin2)
            return dp[i][j]
        
        longest_palin_subsequence = (recurse(0, len(s)-1))
        ans = len(s) - longest_palin_subsequence
        return ans