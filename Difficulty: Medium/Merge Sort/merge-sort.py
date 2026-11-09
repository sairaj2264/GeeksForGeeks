class Solution:
    def mergeSort(self, arr, l, r):
        # code here
        def merge(arr, low, mid, high):
            
            left = low
            right = mid + 1
            temp_arr = []
            while (left <= mid and right <= high):
                if arr[left] <= arr[right]:
                    temp_arr.append(arr[left])
                    left += 1
                else:
                    temp_arr.append(arr[right])
                    right += 1
            
            while (left <= mid):
                temp_arr.append(arr[left])
                left += 1
                
            while (right <= high):
                temp_arr.append(arr[right])
                right += 1
                
            i = 0
            j = low
            while i < len(temp_arr):
                arr[low] = temp_arr[i]
                i += 1
                low += 1
        
        def merge_sort(arr, low,high):
            
            if low >= high:
                return
            
            mid = (low + high)//2
            
            merge_sort(arr, low, mid)
            merge_sort(arr, mid + 1, high)
            merge(arr, low, mid, high)
            
        merge_sort(arr,0 , len(arr)-1)
            
        
        