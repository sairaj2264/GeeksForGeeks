class Solution:
    def getSingle(self, arr):
        # code here 
        
        ones = 0
        twos = 0

        for i in arr:
            ones = (ones ^ i) &(~twos)
            twos = (twos ^ i) &(~ones)
                    
        return ones