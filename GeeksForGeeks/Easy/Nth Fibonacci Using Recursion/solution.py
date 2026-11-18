class Solution:
    def nthFibonacci(self, n):
        # Code here
        def recurse(n):
            if n == 1:
                return 1
            
            elif n == 0:
                return 0
            
            else:
                return (recurse(n-1) + recurse(n-2))
                
        return recurse(n)