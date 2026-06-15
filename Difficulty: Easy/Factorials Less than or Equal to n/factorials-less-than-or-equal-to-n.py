#User function Template for python3

class Solution:
    def factorialNumbers(self, n):
        
        answerList = []
        def factorial(a ,answer, n):
            if answer > n:
                answerList.pop()
                return
            answer = answer * a
            answerList.append(answer)
            factorial(a + 1, answer, n )
            
        factorial(1, 1, n)
        
        return answerList
            
    	#code here 
    	