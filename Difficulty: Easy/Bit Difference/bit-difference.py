class Solution:
    def countBitsFlip(self, a, b):
        #code here
        
        result = a ^ b
        
        count = 0
        while result > 0:
            count += 1
            result = (result & (result -1))
            
        return count