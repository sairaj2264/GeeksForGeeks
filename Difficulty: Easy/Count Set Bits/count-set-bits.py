class Solution:
    def setBits(self, n):
        # code here
        
        count = 0
        for i in range (0, 31):
            temp = 1
            
            if ((temp << i) & n) > 0:
                count += 1
                
        return count
            
            
            