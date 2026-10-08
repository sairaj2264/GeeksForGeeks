class Solution:
    def divide(self, a, b):
        # code here
        
        if b == 0:
            return 2147483647

        is_negative = 0
        if a < 0 and b < 0:
            is_negative = 1
            
        if is_negative == 0:
            if a < 0 or b < 0:
                is_negative = - 1
            else:
                is_negative = 1
        a = abs(a)
        b = abs(b)
        
        quotient = 0
        count = 0
        
        while (a > 0 and a >= b):
            count = 0
            while ( (b * (2 ** count)) <= a):
                count += 1
                
            count -= 1
            a -= (b *(2** count))
            quotient += 2 **count
        
        
        quotient *= is_negative
        return quotient
            