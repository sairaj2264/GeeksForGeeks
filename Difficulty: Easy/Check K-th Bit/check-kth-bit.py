class Solution:
    def checkKthBit(self, n, k):
        # code here
        temp = 1
        
        temp = temp << k
        
        if n & temp > 0:
            return True
        return False