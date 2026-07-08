class Solution:
    def countGreater(self, arr, indices):
        # Code here
        # stack = []
        # hm = {}
        # sum = 0
        answer = []
        for i in range (0,len(indices)):
            # print(i)
            
            index = indices[i]
            count = 0
            for j in range (len(arr) - 1, index - 1, -1):
                if arr[j] > arr[index]:
                    count = count + 1
                    # print(count)
                    
            
            answer.append(count)
            
        
        return answer
        
        # for i in range (len(arr) - 1, -1, -1):
            
        #     if len(stack) == 0:
        #         stack.append(arr[i])
        #         hm[i] = 0
            

        #     elif stack[-1] <= arr[i]:
        #         temp = stack[-1]
        #         while(len(stack) > 0 and temp <= arr[i]):
        #             temp = stack[-1]
        #             stack.pop()
                    
        #         if len(stack) == 0:
        #             stack.append(arr[i])
        #             hm[i] = 0
        #         else:
        #             hm[i] = len(stack)
        #             stack.pop()
                    
        #     else:
        #         hm[i] = len(stack)
        #         stack.append(hm[i])
        # answer = []    
        # print(hm)
        # # for i in indices:
        # #     answer.append(hm[i])
        
        # import heapq
        
        # heap = []
        # answer = []
        # stack = []
        # hm = {}
        
        # for i in range (len(arr) - 1, -1, -1):
        #     if len(heap) == 0:
        #         heapq.heappush(heap, -arr[i])
        #         hm[i] = 0
            
        #     elif abs(heap[0]) >= arr[i]:
        #         while (len(heap) > 0 and abs(heap[0]) > arr[i]):
                    
        #             temp = heapq.heappop(heap)
        #             stack.append(temp)
                
        #         if len(stack) > 0:
        #             hm[i] = len(stack)
        #         else:
        #             hm[i] = 0
                    
        #         while (len(stack) > 0):
        #             temp = stack.pop()
        #             heapq.heappush(heap, temp)
        #         heapq.heappush(heap, -arr[i])
                
        #     else:
        #         hm[i] = 0
        #         heapq.heappush(heap, -arr[i])
                
                
        # for i in indices:
        #     answer.append(hm[i])
        # return answer
            
        
                
                
            
        