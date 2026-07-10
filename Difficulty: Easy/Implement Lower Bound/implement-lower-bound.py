class Solution:
    def lowerBound(self, arr, target):
        # code here
        p1 = 0
        p2 = len(arr)
        answer = p2
        
        if target > arr[-1]:
            return len(arr)
        while (p1 <= p2):
            mid = (p1 + p2)//2
            midVal = arr[mid]
            
            if midVal >= target:
                answer = mid
                p2 = mid - 1
                
            else:
                p1 = mid + 1
                
        return answer
            
            