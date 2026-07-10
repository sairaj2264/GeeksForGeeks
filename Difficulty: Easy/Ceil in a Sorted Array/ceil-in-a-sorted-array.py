class Solution:
    def findCeil(self, arr, x):
        # code here
        
        p1 = 0
        p2 = len(arr) - 1
        
        answer = -1
        while(p1 <=p2):
            mid = (p1 + p2)//2
            

                
            if arr[mid] >= x:
                
                answer = mid
                p2 = mid - 1
                
            elif arr[mid] < x:

                p1 = mid + 1
                
        return answer
                
