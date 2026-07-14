class Solution:
    def findPages(self, arr, k):
        # code here
        
        
        if k > len(arr):
            return -1
        
        if k == len(arr):
            return max(arr)
            
        def checker(nums, k, x):
            
            counter = 1
            summ = 0
            for i in range (0,len(nums)):
                summ += nums[i]
                # print(counter, summ, x)
                if summ > x:
                    counter += 1
                    summ = nums[i]
                # elif summ == x:
                #     counter +=1
                #     summ = 0
                
                if nums[i] > x:
                    return False
            
            # if summ > 0 and counter > 0:
            #     counter += 1
            if counter > k:
                return False
            return True
            
        # print(checker(arr, k, 25))
        
        low = 1
        high = 9999999999
        answer = 0
        while (low <= high):
            mid = (low + high)//2 
            
            if checker(arr, k, mid) == True:
                high = mid - 1

                answer = mid

                    
            else:
                low = mid + 1
                
        return answer
                
                
                