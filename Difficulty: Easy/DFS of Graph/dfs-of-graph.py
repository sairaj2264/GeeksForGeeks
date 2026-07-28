class Solution:
    def dfs(self, adj):
        # code here
        visited = [0] * 10000
        dfs = []
        def recurse(node, dfs, visited):
            if visited[node] == 1:
                return
            dfs.append(node)
            visited[node] = 1
            
            connected = adj[node]
            # print(connected)
            
            for i in range (0 , len(connected)):
                element = connected[i]
                if visited[element] == 0:
                    recurse(element, dfs, visited)
                    
        recurse(0, dfs, visited)
        return dfs