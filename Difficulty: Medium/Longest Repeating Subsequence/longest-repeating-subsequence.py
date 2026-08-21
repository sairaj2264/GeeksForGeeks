class Solution:
	def longestRepSubseq(self, s: str) -> int:
		# Code here
		l1 = len(s) + 1
		l2 = len(s) + 1
		dp = [[-1] * l1 for _ in range(l2)]
		
		def recurse(s,i,j):
		    val1 = 0
		    val2 = 0
		    val3 = 0
		    if i < 0 or j < 0:
		        return 0
		        
		    if dp[i][j] != -1:
		        return dp[i][j]
		    elif s[i] == s[j] and i != j:
		        val1 =  1 + recurse(s,i-1,j-1)
            else:
	            val2 = recurse(s,i,j-1)
	            val3 = recurse(s, i-1, j)
	        
		    temp = max(val1, val2, val3)
		    dp[i][j] = temp
		    return temp
		 
		 
	    return recurse(s,l1-2,l2-2)