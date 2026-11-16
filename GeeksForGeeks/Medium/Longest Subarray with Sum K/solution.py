class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        hm = {}
        prefixSum = 0
        max_length = 0
        
        if len(arr) == 0:
            return 0
            
        for i in range(0,len(arr)):
            prefixSum += arr[i]
            if prefixSum == k:
                max_length = max(max_length, i + 1)
                
                temp = hm.get(prefixSum,-1)
                if temp == -1:
                    hm[prefixSum] = i
            else:
                diff = prefixSum - k
                temp = hm.get(diff,-1)
                if temp == -1:
                    if hm.get(prefixSum,-1) == - 1:
                        hm[prefixSum] = i
                else:
                    ans = (i - temp)
                    max_length = max(max_length, ans)
                    if hm.get(prefixSum,-1) == - 1:
                        hm[prefixSum] = i
        return max_length
            
        
