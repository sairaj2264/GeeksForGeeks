class Solution:    
    def minPlatform(self, arr, dep):
        # code here
        # from collections import OrderedDict
        
        # od = OrderedDict ()
        numsA = arr.copy()
        numsD = dep.copy()
        
        numsA.sort()
        numsD.sort()
        maxx = 0
        
        counter = 0
        
        # print(numsA)
        # print(numsD)
        i = 0
        j = 0
        
        while (i < len(numsA) and j < len(numsD)):
            if (numsA[i] <= numsD[j]):
                counter += 1
                maxx = max(maxx, counter)
                i += 1
            else:
                counter -= 1
                j+= 1
        
            
        
        
        return maxx
                    
                
        