class Solution:
	def perfectSum(self, arr: list[int], target: int) -> int:
		# code here
		
		dp = [[-1] * (target + 2) for _ in range(len(arr) + 2)]
		
		
		def recurse(i,summ):
		    if summ > target              :
                return 0
            
            if i >= len(arr):
                if summ == target:
                    return 1
                return 0
                
            if dp[i][summ] != -1:
                return dp[i][summ]
                
            ans1 = recurse(i+1, summ + arr[i])
            ans2 = recurse(i+1, summ)
            dp[i][summ] = (ans1 + ans2)
            return (ans1 + ans2)
            
        
        return recurse(0,0)