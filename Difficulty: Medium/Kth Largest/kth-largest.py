class Solution:
    def kthLargest(self, arr, k):
        # code here
        
        
        import heapq
        
        heap = []
        
        for i in range(0 , len(arr)):
            heapq.heappush(heap, - arr[i])
            
        element = 0
        for i in range(0 , k):
            element = - heapq.heappop(heap)
            
        return element