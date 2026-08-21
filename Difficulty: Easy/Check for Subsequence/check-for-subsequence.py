class Solution:
    def isSubSeq(self, s1, s2):
        # code here
        
        
        p1 = 0
        p2 = 0
        
        while(p1 < len(s1) and p2 < len(s2)):
            
            if s1[p1] == s2[p2]:
                p1 += 1
                p2 += 1
            else:
                p2 += 1
                
        
        if p1 == len(s1):
            return True
        
        return False
        # l1 = len(s1) + 1
        # l2 = len(s2) + 1
        # dp = [[-1]* l2 for _ in range(l1)]
        
        # def recurse(i,j):
            
        #     val1 = 0
        #     val2 = 0
        #     val3 = 0
            
        #     if i < 0 or j < 0:
        #         return 0
            
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     elif s1[i] == s2[j]:

        #         val1 = 1 + recurse(i - 1,j - 1)
                
        #     else:
        #         val2 = recurse(i-1, j)
        #         val3 = recurse(i,j-1)
            
        #     dp[i][j] = max(val1, val2, val3)
        #     return dp[i][j]
            
        # val = recurse(l1-2,l2-2)
        
        # if val == len(s1):
        #     return True
        # return False
                