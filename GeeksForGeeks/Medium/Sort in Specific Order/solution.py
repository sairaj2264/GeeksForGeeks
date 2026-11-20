class Solution:
    def sortIt(self, arr):
        # code here
        import heapq
        odd_heap = []
        even_heap = []
        answer = []
        
        for i in range(0 , len(arr)):
            element = arr[i]
            if element %2 == 0:
                heapq.heappush(even_heap, element)
            else:
                heapq.heappush(odd_heap, -element)
        
        arr.clear()
        while len(odd_heap) > 0:
            element = -1 * heapq.heappop(odd_heap)
            arr.append(element)
            
        while len(even_heap) > 0:
            element = heapq.heappop(even_heap)
            arr.append(element)
        

        return
