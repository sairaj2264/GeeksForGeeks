class Solution:
    def setBit(self, n):
        # code here
        
        temp = n + 1
        
        temp = temp|n
        
        return(temp)
        