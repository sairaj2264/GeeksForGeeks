class Solution:
    def maxMeetings(self, s, f):
        # code here
        arr = []
        for i in range(0 , len(s)):
            temp = (s[i], f[i], i+1)
            arr.append(temp)
            
        arr.sort(key = lambda x : (x[1], x[2]))
        #O(n)
        #O(nlogn)

        start = 0
        end = -1
        answer = []
        # print(arr)
        
        #O(n)
        for i in range (len(arr)):
            if end < arr[i][0]:
                answer.append(arr[i][2])
                end = arr[i][1]
        answer.sort()
        return answer