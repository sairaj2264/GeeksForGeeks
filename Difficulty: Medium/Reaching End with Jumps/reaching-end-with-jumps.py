class Solution:
    def canReach(self, arr):
        
        max_position = 0
        
        answer = True
        for i in range(0 , len(arr)):
            if max_position < i:
                answer = False
                break
            temp = arr[i] + i
            max_position = max(max_position, temp)
            
        return answer
                
        