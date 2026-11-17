class Solution:
    def numberOfSubarrays(self, arr, target):
        # code here
        total = 0
        i = 0
        j = 0
        temp = 0
        
        
        while j < len(arr):
            temp += arr[j]
            
            next_one = len(arr) - 1
            if temp == target:
                idx = j+1
                while idx < len(arr) and arr[idx] == 0:
                    idx += 1
                next_one = idx - 1
                    
            while temp == target:
                total += 1
                total += (next_one - j)
                temp -= arr[i]
                i+=1
            j+=1
            
        return total
            