class Solution:
	def minOperations(self, s1, s2):
		# code here
		l1 = len(s1) + 1
		l2 = len(s2) + 1
		dp = [[0] * l2 for _ in range(l1)] 
		
		
		for i in range(1 , l1):
		    
		    for j in range(1, l2):
		        
		        if s1[i-1] == s2[j-1]:
		            dp[i][j] = 1 + dp[i-1][j-1]
		           
		        else:
		            if dp[i-1][j] > dp[i][j-1]:
		                dp[i][j] = dp[i-1][j]
		            else:dp[i][j] = dp[i][j-1]
		            
	    lcs = dp[l1-1][l2-1]
	    no_del = len(s1) - lcs
	    no_add = len(s2) - lcs
	    ans = no_del + no_add
	    return ans
		                
		                
		                