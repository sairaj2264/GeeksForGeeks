class Solution:
	def perfectSum(self, arr, target):
		# code here
	    
	    summ = 0
	    for i in range(0 , len(arr)):
	        summ = summ + arr[i]
	        
	    dp = [[-1] * (len(arr) + 1) for _ in range(summ + 1)]
		
		def recurse(arr, target, summ, idx):
		    
		    if idx >= len(arr):
		        if summ == target:
		            return 1
		        return 0
            
            sum1 = 0
            sum2 = 0
            if dp[summ][idx] != -1:
                return  dp[summ][idx]
                
            sum1 = recurse(arr, target, summ, idx + 1)

            sum2 = recurse(arr, target, summ + arr[idx], idx + 1)
            
            dp[(summ)][idx] = (sum1 + sum2)
            
            return dp[(summ)][idx]
            
        
        return recurse(arr, target, 0 , 0)