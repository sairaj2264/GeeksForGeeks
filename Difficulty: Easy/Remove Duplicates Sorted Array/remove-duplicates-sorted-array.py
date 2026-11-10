class Solution:
    def removeDuplicates(self, arr):
        # code here 
        nums = []
        nums.append(arr[0])
        for i in range(1 , len(arr)):
            if arr[i-1] < arr[i]:
                nums.append(arr[i])
        return nums
        
        
        