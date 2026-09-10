class Solution:
    def maxConsecBits(self, arr):
        #code here 
        maxx = 0
        
        oCount = 0
        zcount = 0
        for i in arr:
            if i == 1:
                zcount = 0
                oCount += 1
                
                maxx = max(maxx, oCount)
                
            else:
                zcount += 1
                oCount = 0
                maxx = max(maxx, zcount)
                
        return maxx
                