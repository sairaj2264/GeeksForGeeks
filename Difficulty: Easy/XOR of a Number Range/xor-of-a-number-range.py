class Solution:
    def findXOR(self, l, r):
        # code here
        
        
        def findXor(n):
            if n%4 == 1:
                return 1
            elif n % 4 == 2:
                return (n + 1)                
            elif n % 4 == 3:
                return 0
            elif n % 4 == 0:
                return n
                
                
            
        answer = findXor(l - 1) ^ findXor(r)
        return answer
            
        