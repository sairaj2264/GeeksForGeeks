class Solution:
    def printTillN(self, n):
    	#code here 
    	
    	def printer(i, n):
    	    
    	    if i < 1:
    	        return
    	    printer(i-1 , n)
    	    print(i, "", end = "")
    	    
    	printer(n,n)
    	