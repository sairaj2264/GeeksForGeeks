class Solution:
    def intersection(self, arr1, arr2):
        #code here
        sett = []
        l1 = 0
        l2 = 0
        r1 = len(arr1)
        r2 = len(arr2)
        
        while l1 < r1 and l2 < r2:
            if arr1[l1] == arr2[l2]:
                if len(sett) == 0 or sett[-1] != arr1[l1]:
                    sett.append(arr1[l1])
                l1 += 1
                l2 += 1
            
            elif arr1[l1] < arr2[l2]:
                l1 += 1
                
            else:
                l2 += 1
        
        
            
        return sett
                
            
