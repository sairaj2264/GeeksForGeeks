class Solution:
    def topoSort(self, V: int, edges: list[list[int]]) -> list[int]:
        # Code here
        
        from collections import defaultdict
        hm = defaultdict(list)
        stack = []
        visited = [0] * V
        for i in range (0 , len(edges)):
            hm[edges[i][0]].append(edges[i][1])
            # hm[edges[i][1]].append(edges[i][0])
            
        # print(hm)
        
        def dfs(hm, element, visited, stack):
            if visited[element] == 1:
                return
            visited[element] = 1

            elements = hm[element]
            
            for i in range( 0 , len(elements)):
                dfs(hm, elements[i], visited, stack)
            stack.append(element)
                
        
        
        
        for i in range(0, len(visited)):
            if visited[i] == 0 :
                dfs(hm,i, visited, stack)
                
        stack = stack[::-1]
        
        # print(stack)
        
        return stack