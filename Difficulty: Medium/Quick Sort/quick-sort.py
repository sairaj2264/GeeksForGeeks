class Solution:
    def quickSort(self, arr, low, high):
        # code here
        if low < high:
            partition_index = self.partition(arr,low,high)
            self.quickSort(arr, low, partition_index-1)
            self.quickSort(arr, partition_index+1, high)

    def partition(self, arr, low, high):
        # code here
        pivot = arr[low]
        
        left = low + 1
        right = high
        while (left <= right):
            while (left <= right and arr[left] <= pivot):
                left += 1
            
            while (left <= right and arr[right] >= pivot):
                right -= 1
            
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
            
        arr[right], arr[low] = arr[low], arr[right]
        return right