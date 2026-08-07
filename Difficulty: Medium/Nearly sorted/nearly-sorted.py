class Solution:
    def nearlySorted(self, arr, k):  
        #code here
        import heapq
        
        heap = []
        n = len(arr)
        i = 0
        while (k < n and i < k):
            heapq.heappush(heap, arr[i])
            i+=1
        j = 0
        while (i < n):
            heapq.heappush(heap, arr[i])
            element = heapq.heappop(heap)
            arr[j] = element
            j += 1
            i += 1
            
            
        while(j < n):
            element = heapq.heappop(heap)
            arr[j] = element
            j += 1
            
        