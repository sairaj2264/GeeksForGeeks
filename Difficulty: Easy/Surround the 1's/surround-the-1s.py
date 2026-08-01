class Solution:
	def Count(self, matrix):
		# Code here
		
		
		count = 0
		for k in range (0 , len(matrix)):

		    for l in range(0 , len(matrix[0])):
		        cnt = 0
		        if matrix[k][l] == 1:
            	    for i in range (-1, 2):
            	        for j in range(-1, 2):
            	            
            	            if i == 0 and j == 0:
            	                continue
            	            elif (k + i) >=len(matrix) or (k + i) < 0:
            	                continue
            	            
            	            elif ( l + j) >= len(matrix[0]) or (l + j) < 0:
            	                continue
            	            
            	            if matrix[k + i][l + j] == 0:
            	                cnt+=1
            	                
            # 	print(cnt)
            	if cnt % 2 == 0 and cnt > 0:
            	    count += 1
            	    
        return count
    	            
	            