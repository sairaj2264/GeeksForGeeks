class Solution:
    def minTime(self, arr, k):
        # code here
        
        def checker(nums, k, x):
            counter = 1
            summ = 0
            
            for i in range (0, len(nums)):
                if nums[i] > x:
                    return False
                    
                summ += nums[i]

                if summ > x:
                    counter += 1
                    summ = nums[i]
                    
            
            if counter > k:
                return False
            return True
            
            
        # print(checker(arr, k , 36))
            
            
            
            
        low = 1
        high = 999999
        answer = 0
        while (low <= high):
            
            
            mid = (low + high)//2
            if checker(arr, k , mid) == True:
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return answer
            