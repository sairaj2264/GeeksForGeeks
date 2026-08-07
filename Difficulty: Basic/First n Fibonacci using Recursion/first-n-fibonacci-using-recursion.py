class Solution:
    #Function to return list containing first n fibonacci numbers.
    def fibonacciNumbers(self,n):
        # your code here
        answer = []
        dp = [-1] * ( n + 1)
        
        def fibo(n, dp):
            
            if n <= 1:
                return n
                
            if dp[n] != -1:
                return dp[n]
                
            dp[n] = (fibo(n-1, dp) + fibo(n-2, dp))
            
            return dp[n]
            
        dp[0] = 0
        dp[1] = 1
        
        
        fibo(n, dp)
        dp.pop()
        return dp
                