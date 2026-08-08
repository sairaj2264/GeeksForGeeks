class Solution:
    def nthTribonacci(self, n: int) -> int:
        # code here
        
        arr = [0]* (n + 1)
        
        
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        elif n == 2:
            return 1
        
        
        
        arr[0] = 0
        arr[1] = 1
        arr[2] = 1
        for i in range(3 , n + 1):
            temp = arr[i-3] + arr[i-2] + arr[i-1]
            arr[i] = temp
            
        return arr[-1]
            
