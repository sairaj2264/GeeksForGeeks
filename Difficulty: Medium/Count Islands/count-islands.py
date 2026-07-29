class Solution:
    def numIslands(self, grid):
        # code here
        from collections import deque
        
        q = deque()
        n = len(grid)
        m = len(grid[0])
        visited = [ [0] * (m) for i in range(n)]
        # print(visited)
        counter = 0
        
        def traverse(i , j, n ,m, visited):
            if visited[i][j] == 1:
                return
            
            visited[i][j] = 1
            
            if (i-1) >= 0 and (j-1) >= 0:
                if grid[i-1][j-1] == 'L':
                    q.append((i-1, j-1))
                    # visited[i-1][j-1] = 1
            
            if (i-1) >= 0:
            
                if grid[i-1][j] == 'L':
                    q.append((i-1, j))
                    # visited[i-1][j] = 1
            
                if (j+1) < m and grid[i-1][j+1] == 'L':
                    q.append((i-1, j+1))
                    # visited[i-1][j+1] = 1
            
            if (j-1) >= 0:
            
                if (i+1) < n and grid[i+1][j-1] == 'L':
                    q.append((i+1, j-1))
                    # visited[i+1][j-1] = 1
            
                if grid[i][j-1] == 'L':
                    q.append((i, j-1))
                    # visited[i][j-1] = 1
            
            if (j+1) < m and grid[i][j+1] == 'L':
                q.append((i, j+1))
                # visited[i][j+1] = 1
            
            if (i+1) < n and grid[i+1][j] == 'L':
                q.append((i+1, j))
                # visited[i+1][j] = 1
            
            if (i+1) < n and (j+1) < m and grid[i+1][j+1] == 'L':
                q.append((i+1, j+1))
                # visited[i+1][j+1] = 1
            
            while (len(q) > 0):
                
                element = q.popleft()
                i , j = element[0], element[1]
                if visited[i][j] == 0:
                    traverse(i , j, n ,m, visited)
        
        for i in range (0 , len(visited)):
            for j in range (0 , len(visited[i])):
                if grid[i][j] == 'L' and visited[i][j] == 0:
                    counter += 1
                    traverse(i , j, n , m, visited)
                    
        
        return counter
                    