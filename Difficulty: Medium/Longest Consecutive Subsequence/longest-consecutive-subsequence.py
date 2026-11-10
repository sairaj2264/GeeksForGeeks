class Solution:
    def longestConsecutive(self, arr):
        # code here
        sett = set()
        
        for i in range(0 , len(arr)):
            sett.add(arr[i])
            
        max_length = 0
        
        for element in sett:
            idx = element - 1
            
            if idx in sett:
                continue
            else:
                counter = 0
                idx += 1
                while(idx in sett):
                    counter += 1
                    max_length = max(max_length, counter)
                    idx += 1
        return max_length
                    
                    
            