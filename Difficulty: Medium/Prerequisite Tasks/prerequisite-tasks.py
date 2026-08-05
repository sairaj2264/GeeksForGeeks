class Solution:
    def isPossible(self, n, pre):
        # code here
        
        from collections import defaultdict
        
        hm = defaultdict(list)
        visited = [0] * n
        
        
        counter = 0
        for i in range(0 , len(pre)):
            hm[pre[i][1]].append(pre[i][0])
            
        
        # print(hm )
        def dfs(hm, visited, element):
            nonlocal counter
            if visited[element] == 1:
                return False
                
            if visited[element] == 2:
                return True
            
            visited[element] = 1
            
            elements = hm[element]
            
            for i in range(0 , len(elements)):
                if dfs(hm, visited, elements[i]) == False:
                    return False
                
            visited[element] = 2
            counter += 1
            return True
            
        for i in range(n):
            if visited[i] == 0:
                ans = dfs(hm, visited, i)
                if ans == False:
                    return False
                            
        return True
        
        
        