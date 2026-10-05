class Solution:
    def leastWeightCapacity(self, arr, d):
        # code here
        
        if d == 1:
            return sum(arr)
        def shipper(nums, days,capacity):
            i = 0
            answer = 0
            weight = 0
            while i < len(arr):
                if arr[i] > capacity:
                    return False
                
                weight += nums[i]
                if weight > capacity:
                    answer += 1
                    weight = nums[i]
                    i+=1
                elif weight == capacity:
                    answer += 1
                    weight = 0
                    i+=1
                else:
                    i+=1
                    
            if weight > 0:
                answer += 1
                
            if answer > days:
                return False
            return True
            
        
        
        low = 1
        high = 10**9
        answer = -1
        while(low <= high):
            mid = (low + high)//2
            # print(mid)
            
            temp = shipper(arr,d,mid)
            if temp == False:
                low = mid + 1
                
            elif temp == True:
                if shipper(arr, d, mid-1) == False:
                    answer = mid
                    break
                else:
                    high = mid - 1
                    
        return answer
        
                            
            
            