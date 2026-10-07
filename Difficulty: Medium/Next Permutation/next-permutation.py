class Solution:
    def nextPermutation(self, arr):
        # code here
        
        flag = False
        index1 = None
        index2 = None
        
        n = len(arr)
        i = n - 1
        
        while (i > 0):
            if arr[i] > arr[i-1]:
                flag = True
                index1 = i - 1
                break
            i-=1
            
        if flag == False:
            arr.sort()
            return arr
        i = n - 1
        
        while (i > -1):
            if arr[i] > arr[index1]:
                index2 = i
                break
            i-=1
            
        arr[index1], arr[index2] = arr[index2], arr[index1]
        
        arr[index1+1:] = sorted(arr[index1+1:])
        return arr
        
            
            