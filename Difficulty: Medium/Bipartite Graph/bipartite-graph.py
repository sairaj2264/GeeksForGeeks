class Solution:
    def isBipartite(self, V, edges):
        # code here
        from collections import defaultdict
        
        hm = defaultdict(list)
        
        for i in range(0 , len(edges)):
            
            elements = edges[i]
            
            hm[elements[0]].append(elements[1])
            hm[elements[1]].append(elements[0])
            
        # print(hm)
                
        visited = [-1] * 200001
        def bfs(hm , visited, current, index, ans):
            if current == 0:
                current = 1
            else:
                current = 0
                
            if ans == False:
                return False
            
            if visited[index] != -1 and visited[index] != current:
                return False
                    
            elif visited[index] != -1:
                return True
            
            visited[index] = current
            elements = hm[index]
            for i in range(0 , len(elements)):
                ans = bfs(hm , visited, current, elements[i], ans)
                if ans == False:
                    break
                
            return ans
            
        anss = bfs(hm , visited, 0 , 0, True)
        return anss
                
            
            
            
            
            
            
            
            
            
            