class Solution:
    def kthMissing(self, arr, k):
        # code here
        
        low = 0
        high = len(arr) - 1
        
        while (low <= high):
            mid = (low + high)//2
            temp = arr[mid] - (mid + 1)
            if temp >= k:
                high = mid - 1
                
            else:
                low = mid + 1
                
        return low + k
               