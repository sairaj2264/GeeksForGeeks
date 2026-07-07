class Solution:
    from collections import deque
	def nextSmallerEle(self, arr):
		# code here
	    stack = []
		
		hm = {}
		for i in range (len(arr) -1,-1, -1):
		  #  print(hm)
		    if len(stack) == 0:
		        stack.append(arr[i])
		        hm[i] = -1
		        
		    elif stack[-1] < arr[i]:
		        hm[i] = stack[-1]
		        stack.append(arr[i])
		    
		    elif stack[-1] >= arr[i]:
		        while len(stack) != 0 and stack[-1] >= arr[i]:
		            stack.pop()
		        if len(stack) > 0:
		            hm[i] = stack[-1]
		        else:
		            hm[i] = -1
		        stack.append(arr[i])
		    
# 		print(hm) 
		answer = []
		for i in range (0, len(hm)):
		    answer.append(hm[i])
		    
		return answer
		    