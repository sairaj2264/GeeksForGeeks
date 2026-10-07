class Solution:
    def jobSequencing(self, deadline, profit):
        # code here
        import heapq
        heap = []
        
        
        nums = sorted(zip(deadline, profit), key =  lambda x:x[0])
        # print(nums)
        
        profit = 0
        count = 0 
        for i in range (0 , len(nums)):
            temp_deadline = nums[i][0]
            temp_profit = nums[i][1]
            
            if len(heap) > 0:
                min_profit = heap[0]
                size = len(heap)
            else:
                min_profit = 0
                size = 0
            
            if size < temp_deadline:
                heapq.heappush(heap, temp_profit)
                profit += temp_profit
                count += 1
                
            elif size == temp_deadline:
                if temp_profit > min_profit:
                    temp = heapq.heappop(heap)
                    heapq.heappush(heap,temp_profit)
                    profit -= temp
                    profit += temp_profit
                    
        return [count, profit]
                    
                    
        
        
        