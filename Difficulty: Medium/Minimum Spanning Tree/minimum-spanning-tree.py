class Solution:
    def spanningTree(self, V: int, edges: list[list[int]]) -> int:
        # code here
        import heapq
        from collections import defaultdict
        mst = []
        heap = []
        visited = [0] * (V)
        adj = defaultdict(list)
        
        answer = 0
    
        
        for source, target, weight in edges:
            adj[source].append((target, weight))
            adj[target].append((source, weight))
            
        
        heapq.heappush(heap, (0,0))
        
        while len(heap) > 0:
            weight , target = heapq.heappop(heap)
            if visited[target] == 1:
                continue
            visited[target] = 1
            connections = adj[target]
            answer += weight
            
            for destination, weight in connections:
                heapq.heappush(heap, (weight, destination))
                    
        return answer
    