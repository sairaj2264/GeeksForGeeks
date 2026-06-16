class Solution:
    def missingNum(self, arr):
        n = len(arr)
        n = n+1
        summ = (n*(n+1))/2
        
        summ2 = 0
        for i in range (0,n-1):
            summ2 += arr[i]
            
        
        answer = int(summ - summ2)
        
        return answer
            
        # code here
        