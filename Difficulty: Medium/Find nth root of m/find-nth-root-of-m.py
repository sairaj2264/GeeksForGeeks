class Solution:
    def nthRoot(self, n, m):
       # code here
       
        if n == 1 and m == 1:
            return 1
           
        if m == 0:
            return 0
        low = 1
        high = m
        
        while (low <= high):
            
            mid = (low + high)//2
            temp = mid ** n
            
            if temp == m:
                return mid
                
            elif temp != m and low == high:
                return -1
                
            elif temp > m:
                high = mid - 1
            
            else:
                low = mid + 1
                
        return -1
