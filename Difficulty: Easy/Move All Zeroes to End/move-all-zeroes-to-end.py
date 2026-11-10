class Solution:
	def pushZerosToEnd(self, arr: list[int]) -> None:
    	# code here
    	i = 0
    	j = 0
    	
    	while j < len(arr):
    	    if arr[j] == 0:
    	        i = j
    	        break
    	    j+=1
    	
    	while j < len(arr):
    	    if arr[j] != 0:
    	        arr[i], arr[j] = arr[j], arr[i]
    	        i+=1
    	        j+=1
    	    else:
    	        j+=1
    	        
    	 
    	    