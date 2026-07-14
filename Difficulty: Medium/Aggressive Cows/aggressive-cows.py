class Solution:
    def aggressiveCows(self, arr, k):
        
        # code here
        arr.sort()
        
        def possible(nums, n, x):
            
            
            if x == 1:
                return True
            temp = nums[0]
            counter = 1
            for i in range (1, len(nums)):
                if nums[i] - temp >= x:
                    counter += 1
                    temp = nums[i]
                
            if counter >= n:
                return True
            else:
                return False
                
        
        low = 1
        high = 100000001
        answer = 1
        while (low <= high):
            mid = (low + high)//2
            
            if possible(arr, k, mid) == True:
                low = mid + 1
                answer = mid
            
            else:
                high = mid - 1
                
        return answer
        # print(possible(arr, k , 4))
        # return 1
        
        
                    
                
                
                
        
        