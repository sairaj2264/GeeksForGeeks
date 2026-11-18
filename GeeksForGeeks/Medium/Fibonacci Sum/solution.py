class Solution:
    def fibSum(self, n):
        #code here
        summ = 0
        dp = [-1] * (n +1)
        def recurse(n):
            nonlocal summ
            if n == 1:
                if dp[n] == -1:
                    summ += 1
                    dp[n] = 1
                    return 1
                else:
                    return 1
            
            elif n == 0:
                return 0
                
        
            if dp[n] == -1:
                temp =  (recurse(n - 1) + recurse(n - 2))
                dp[n] = temp % 1000000007
                summ += temp
                summ = summ % 1000000007
                return temp
            
            else:
                return dp[n]
                
                
        recurse(n)
        return summ % 1000000007