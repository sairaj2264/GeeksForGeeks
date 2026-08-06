class Solution:
    def isMaxHeap(self, arr):
        # code here
        flag = True
        
        for i in range(0 , len(arr)):
            if flag == False:
                break
            
            idx1 = (2 * i) + 1
            idx2 = (2 * i) + 2
            
            element1 = 0
            element2 = 0
                
            if idx1 < len(arr):
                element1 = arr[idx1]
            
            if idx2 < len(arr):
                element2 = arr[idx2]
                
            if arr[i] < element1 or arr[i] < element2:
                flag = False
        
        return flag
