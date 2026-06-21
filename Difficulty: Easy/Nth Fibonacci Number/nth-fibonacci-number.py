class Solution:
    def nthFibonacci(self, n: int) -> int:
        
        #code here
        
        def nthFiboCalculator(n):
            if n <=1:
                return n
                
            return nthFiboCalculator(n-1) + nthFiboCalculator(n-2)
        
        
        return nthFiboCalculator(n)
        