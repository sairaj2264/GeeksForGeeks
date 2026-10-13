class Solution:
    def bellmanFord(self, V: int, edges: list[list[int]], src: int) -> list[int]:
        #code here
        
        distance = [100000000] * V
        distance[src] = 0
        
        for i in range(0 , V):
            for j in range(0,len(edges)):
                u ,v, wt = edges[j]
                if distance[u] == 100000000:
                    continue
                new_wt = distance[u] + wt
                distance[v] = min(distance[v], new_wt)

        for i in range(0 , len(edges)):
            u,v,wt = edges[i]
            new_wt = distance[u] + wt

            if distance[u] == 100000000:
                continue
            if distance[v] > new_wt:
                distance = [-1]
                break
            
        return distance
                
                
        