class Solution:
    def findTwoElement(self, arr):
        # code here
        temp = 0
        
        n = len(arr)
        
        nums = [0] * (n + 1)
        
        for i in range(0 , n):
            nums[arr[i]] += 1
            
        answer1 = -1
        answer2 = -1
        for i in range(1,(n + 1)):
            if nums[i] == 0:
                answer1 = i
            elif nums[i] == 2:
                answer2 = i
            
        
            
        if answer1 == -1:
            answer1 = n + 1
        return ([answer2,answer1])
