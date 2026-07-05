class Solution:
    def findDuplicates(self, arr):
        # code here
        hm = {}
        n = len(arr)
        
        for i in range(0,n):
            hm[arr[i]] = hm.get(arr[i], 0) + 1
            
        answer = []
        for i in hm:
            if hm[i] > 1:
                answer.append(i)
        
        return answer