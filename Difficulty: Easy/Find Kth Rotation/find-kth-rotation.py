class Solution:
    def findKRotation(self, arr):
        # code here
        low = 0
        high = len(arr) - 1
        answer = 0
        while (low <= high):
            mid = (low + high)//2
            
            if arr[low] <= arr[mid]:
                
                if arr[mid] <= arr[high]:
                    answer = low
                    break
                
                else:
                    if arr[mid] < arr[mid + 1]:
                        low = mid
                    else:
                        low = mid + 1
            
            else:
                if arr[mid] < arr[mid + 1]:
                    high = mid
                else:
                    high = mid + 1
                    
        return answer
                
                    
                    