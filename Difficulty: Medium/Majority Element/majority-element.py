class Solution:
    def majorityElement(self, arr):
        #code here
        count = 1
        majority_element = arr[0]
                
        for i in range(1, len(arr)):
            if arr[i] == majority_element:
                count += 1
            else:
                count -= 1
            if count == 0:
                count = 1
                majority_element = arr[i]
        
        countt = 0
        for i in arr:
            if i == majority_element:
                countt += 1
                
        if countt > len(arr)//2:
            return majority_element
        return -1
            
        
        