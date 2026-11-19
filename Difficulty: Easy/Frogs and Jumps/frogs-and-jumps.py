class Solution:

    def unvisitedLeaves(self, arr, k):
        """code here"""
        
            
        nums  = [-1] * (k+1)
        nums[0] = 1
        
        for i in range(0 , len(arr)):
            jump = arr[i]
            j = jump
            while j <= k:
                nums[j] = 1
                j = j + jump
                
        
        answer = 0
        for i in nums:
            if i == -1:
                answer += 1
                
        return answer
            