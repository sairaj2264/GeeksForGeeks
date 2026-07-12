class Solution:
    def floorSqrt(self, n): 
        # code here
        
        if n == 1:
            return 1
        
        low = 1
        high = 30000
        
        while (low <= high):
            mid = (low+high)//2
            
            square = mid * mid
            nextSquare = (mid + 1) * (mid + 1)
            if square <= n and nextSquare > n:
                return mid
                
            elif square > n:
                high = mid - 1
                
            else:
                low = mid + 1
                
        