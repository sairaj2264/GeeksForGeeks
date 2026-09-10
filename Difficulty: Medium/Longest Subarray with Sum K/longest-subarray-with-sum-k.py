class Solution:
    def longestSubarray(self, arr, k):  
        # code here

        hm = {}

        prefix = 0
        answer = 0
        hm[prefix] = -1

        for i in range(len(arr)):
            prefix += arr[i]
            temp = prefix - k

            if temp in hm:
                lenn = i - hm[temp]
                answer = max(answer, lenn)

            if prefix not in hm:
                hm[prefix] = i

        return answer