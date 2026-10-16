class Solution:

    def maxValue(self, n: int) -> int:
        """code here"""
        
        if n == 0:
            return 0
        
        
        cons_ones = 0
        i = 1
        i = i<<31
        
        while (i > 0):
            if (i & n) > 0:
                cons_ones += 1
            else:
                cons_ones = 0
            if cons_ones == 3:
                n = n ^ i
                cons_ones = 0
                
            i = i >> 1
                
                
                
            
        return n
            
            
            
            
            
