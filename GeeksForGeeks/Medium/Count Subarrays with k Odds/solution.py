class Solution:
    def countSubarrays(self, arr, k):
        # Code here
        total = 0
        i = 0
        j = 0
        current_odds = 0
        
        def next_odd(j):
            j += 1
            
            while j < len(arr) and arr[j] % 2 == 0:
                j += 1
                
            if j <= len(arr):
                return j
            return -1
        
        while j < len(arr):
            if arr[j]%2 == 1:
                current_odds += 1
                
                temp = -1
                idx = -1
                if current_odds == k:
                    total += 1
                    temp = next_odd(j)
                    if temp != -1:
                        idx = temp - 1
                        total += idx - j
                
                while current_odds == k and i <= j:
                    if arr[i] % 2 == 1:
                        current_odds -= 1
                        i+=1
                    else:
                        if idx != -1:
                            total += 1 + idx - j
                        else:
                            total += 1
                        i += 1
                
            
            j += 1
        
        return total
            
        
                    
                    