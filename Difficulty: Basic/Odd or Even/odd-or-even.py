class Solution:
    def isEven (self, n):
        # code here 
        
        if n & 1 > 0:
            return False
        return True
        