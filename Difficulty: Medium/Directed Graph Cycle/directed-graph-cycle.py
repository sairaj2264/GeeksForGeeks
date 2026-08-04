class Solution:
    def isCyclic(self, V: int, edges: list[list[int]]) -> bool:
        # code here
        from collections import defaultdict
        
        hm = defaultdict(list)
        visited = [-1] * V
        
        for i in range(0 , len(edges)):
            element = edges[i]
            
            hm[element[0]].append(element[1])
            # hm[element[1]].append(element[0])
            
        # print(hm)
        
        def dfs(visited,idx,current):

            if visited[idx] == current:
                return True
            
            elif visited[idx] == 0:
                return False
                
            visited[idx] = current
                
            elements = hm.get(idx, [])
            
            final = False
            for i in range(0 , len(elements)):
                child  = elements[i]
                final = dfs(visited, child ,current)
                if final == True:
                    return True
            
            visited[idx] = 0
            
            return final
        answer = False
        for key in hm:
            if visited[key] == -1:
               answer = dfs(visited,key,1)
            if answer == True:
                return True
        return answer   
        