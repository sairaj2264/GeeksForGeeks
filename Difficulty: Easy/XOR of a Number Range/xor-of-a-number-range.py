class Solution:
    def findXOR(self, l, r):
        # code here
        
        def xor_function(number):
            quotient = number % 4
            
            if quotient == 0:
                return number
                
            elif quotient == 1:
                return 1
                
            elif quotient == 2:
                return number + 1
            
            else:
                return 0
                
        answer = xor_function(l-1) ^ xor_function(r)
        return answer