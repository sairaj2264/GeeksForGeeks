class Solution:
    def totalElements(self, arr):
        # Code here
        max_len = 0
        hm = {}
        i = 0
        j = 0
        
        running_len = 0
        
        while i < len(arr):
            element = arr[i]
            hm[element] =  hm.get(element, 0) + 1
            running_len += 1
            
            if len(hm) > 2:
                while len(hm) > 2:
                    temp_element = arr[j]
                    hm[temp_element] -= 1
                    if hm[temp_element] <= 0:
                        hm.pop(temp_element)
                    running_len -= 1
                    j += 1
            max_len = max(max_len, running_len)
            i += 1
            
        return max_len
            
            
            
        