class Solution:
    def longestBitonicSequence(self, n, nums):
        # code here
        max_increasing = 1
        max_decreasing = 1
        
        increasing = [1] * n
        decreasing = [1] * n
        
        for i in range(1 ,len(nums)):
            
            for j in range(0 , i):
                
                if nums[i] > nums[j]:
                    
                    if increasing[i] < increasing[j] +1:
                        increasing[i] = increasing [j] + 1
                        max_increasing = max(max_increasing, increasing[i])
        
        nums = nums[::-1]
        
        for i in range(1 ,len(nums)):
            
            for j in range(0 , i):
                
                if nums[i] > nums[j]:
                    
                    if decreasing[i] < decreasing[j] +1:
                        decreasing[i] =  decreasing[j] + 1
                        max_decreasing = max(max_decreasing, decreasing[i])
        
        answer = 0
        decreasing = decreasing[::-1]
        for i in range(len(increasing)):
            if increasing[i] > 1 and decreasing[i] > 1:
                temp = increasing[i] + decreasing[i] -1
            
                answer = max(answer, temp)
            
        
        return answer
            
        # def recurse(i,bitonic, prev):
        #     if i >= len(nums):
        #         return 0
            
        #     if bitonic == 0:
        #         if prev == -1 or nums[i] > nums[prev]:
        #             ans1 = 1 + recurse(i+1,bitonic,i)
        #             ans2 = recurse(i+1, bitonic, prev)
        #             ans3 = 1 + recurse(i+1, bitonic + 1, i)
        #             ans4 = recurse(i+1, bitonic+1, prev)
        #             return max(ans1, ans2, ans3, ans4)
                
        #         else:
        #             ans1 = recurse(i+1, bitonic, prev)
        #             ans2 = recurse(i+1, bitonic+1, prev)
        #             return max(ans1, ans2)
                    
        #     if bitonic == 1:
        #         if prev == -1 or nums[i] < nums[prev]:
                    
                
            
        #     if bitonic == 1:
                