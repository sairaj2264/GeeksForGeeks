class Solution:
    def shortestPath(self, V, edges, src, dest):
        # code here
        from collections import defaultdict
        import heapq
        
        adj = defaultdict(list)
        heap = []
        
        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)
            
        
        count = 0
        for key in adj.keys():
            if key == src or key == dest:
                count += 1
                
        if count < 2:
            return -1
            
        distance = [float('inf')] * V
        
        distance[src] = 0
        heapq.heappush(heap,(0,src))
        
        while len(heap) > 0:
            length ,node = heapq.heappop(heap)
            connections = adj[node]
            for connection in connections:
                new_length = length + 1
                if new_length < distance[connection]:
                    distance[connection] = new_length
                    heapq.heappush(heap,(new_length,connection))
                    
        
        answer = distance[dest]
        if answer == float('inf'):
            return -1
            
        return answer
        
            
        