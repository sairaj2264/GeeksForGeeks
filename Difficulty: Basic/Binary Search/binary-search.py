class Solution:
    def binarySearch(self, arr, k):
        # code here
        
        low = 0
        high = len(arr)- 1
        
        flag = False
        
        while (low <= high):
            
            mid = (low + high)//2
            
            if arr[mid] == k:
                flag = True
                break
            
            elif arr[mid] > k:
               high = mid - 1
               
            else:
                low = mid + 1
            
            
        if flag == True:
            return True
        else:
            return False