class Solution:
    def minMaxDist(self, stations, k):
        # Code here
        
        import heapq
        
        heap = []
        arr = []
        nums = []
        
        if len(stations) == 1:
            return 0.00
        
        
        for i in range (1, len(stations)):
            temp = stations[i]  - stations[i -1]
            arr.append(1)
            nums.append(temp)
            temp = -1 * temp
            heapq.heappush(heap, (temp, i - 1))
            
        # print(arr)
        # print(heap)
        # print(nums)
        
        while (k > 0):
            temp = heapq.heappop(heap)
            # print(temp)
            # heap.pop()
            # divident = abs(temp[0])
        
            index = temp[1]
            divident = nums[index]
            
            divisor = arr[index] + 1
            arr[index] += 1
            
            answer = round(divident/divisor, 6)
            answer = -1 * answer
            
            heapq.heappush(heap, (answer, index))
            
            k -= 1
            
            
            
        answer = abs(heap[0][0])
        
        return answer
        # return 1
        
        # # while (k > 0)