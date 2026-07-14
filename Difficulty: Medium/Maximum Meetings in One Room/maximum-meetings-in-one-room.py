class Solution:
    def maxMeetings(self, s, f) :
        # code here'
        position = []
        order = []
        temp = -1
        
        for i in range (0,len(s)):
            position.append(i+1)
        arr = list(zip(s,f, position))

        
        arr.sort(key=lambda x: (x[1], x[2]))
        # print(arr)
        # return(0,0)
        
        for i in range (len(arr)):
            if arr[i][0] > temp:
                temp = arr[i][1]
                order.append(arr[i][2])
                order.sort()
                
                
        return order
                
        