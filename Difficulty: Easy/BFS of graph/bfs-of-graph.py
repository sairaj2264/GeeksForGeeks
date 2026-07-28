class Solution:
    def bfs(self, adj):
        # code here
        
        from collections import deque
        
        q = deque()
        
        q.append(0)
        bfs = []
        visited = [0] *10000
        while(len(q) > 0):
            temp = q.popleft()
            if visited[temp] == 0:
                visited[temp] = 1
                bfs.append(temp)
                for i in range(0, len(adj[temp])):
                    element = adj[temp][i]
                    if visited[element] == 0:
                        q.append(element)
                        
        return bfs
                        
            
        