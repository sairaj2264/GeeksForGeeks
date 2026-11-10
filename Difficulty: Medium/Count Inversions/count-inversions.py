class Solution:
    def inversionCount(self, arr):
        # code here
        
        count = 0
        
        def merge(arr,low, mid, high):
            nonlocal count
            l1 = low
            r1 = mid
            temp = []
            
            l2 = mid + 1
            r2 = high
            
            while (l1 <= r1 and l2 <= r2):
                if arr[l1] <= arr[l2]:
                    temp.append(arr[l1])
                    l1 +=1
                else:
                    count += (r1 - l1 + 1)
                    temp.append(arr[l2])
                    l2 += 1
            
            while (l1 <= r1):
                temp.append(arr[l1])
                l1 += 1
                
            while (l2 <= r2):
                temp.append(arr[l2])
                l2 += 1
            idx = 0
            for i in range(low, high+1):
                arr[i] = temp[idx]
                idx += 1
        
                    
                
            
        
        def merge_sort(arr, low, high):
            if low < high:
                mid = (low + high)//2
                merge_sort(arr, low, mid)
                merge_sort(arr, mid+1, high)
                merge(arr, low, mid, high)
                
        high = len(arr) -1
        merge_sort(arr, 0 , high)
        return count
            
            
