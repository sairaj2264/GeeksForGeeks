class Solution:
    def printNos(self, n):
        # Code here
        
        def printer(i, n):
            if i > n:
                return
            printer(i+1 , n)
            print(i, "", end = "")
            
        printer(1, n)
            