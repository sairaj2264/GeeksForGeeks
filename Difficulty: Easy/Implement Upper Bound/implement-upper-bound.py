class Solution:
    def upperBound(self, arr, target):
        # code here
        p1 = 0
        p2 = len(arr) - 1
        answer = len(arr)
        
        if target < arr[0] or target > arr[-1]:
            return answer
        while (p1 <= p2):
            mid = ( p1 + p2)//2
            midVal = arr[mid]
            
            if midVal > target:
                answer = mid
                p2 = mid -1
                
            elif midVal == target:
                p1 = mid + 1
            
            else:
                # answer = p2
                p1 = mid  +1
                
        return answer
                