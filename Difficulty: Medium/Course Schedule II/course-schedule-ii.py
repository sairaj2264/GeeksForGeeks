class Solution:
    def findOrder(self, n, prerequisites):
        # code here 
        
        from collections import defaultdict, deque
        answer = []
        hm = defaultdict(list)
        q = deque()
        in_degree = [0]*n
        visited = [0] * n
        
        for i in range(0, len(prerequisites)):
            hm[prerequisites[i][1]].append(prerequisites[i][0])
            
        # print(hm)
        for key in hm:
            elements = hm[key]
            for i in range(0 , len(elements)):
                in_degree[elements[i]] += 1
                
        # print(in_degree)
        
        for i in range(0, len(in_degree)):
            if in_degree[i] == 0:
                q.append(i)
                answer.append(i)
                
            
            
        while(len(q) > 0):
            element = q.popleft()
            elements = hm[element]
            
            for i in range(0 , len(elements)):
                in_degree[elements[i]] -= 1
                if in_degree[elements[i]] == 0:
                    q.append(elements[i])
                    answer.append(elements[i])
                    
                    
        # print(answer)
        if len(answer) != n:
            return []
        return answer
                    
                    
                    
                    