'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def postOrder(self, root):
        # code here
        answer = []
        stack1 = []
        stack2 = []
        
        if root is not None:
            stack1.append(root)

        while(len(stack1) > 0):
            temp = stack1.pop()
            stack2.append(temp)

            
            if temp.left is not None:
                stack1.append(temp.left)
                
            if temp.right is not None:
                stack1.append(temp.right)


                
        while (len(stack2) > 0):
            answer.append(stack2.pop().data)
            
        return answer
                
            
            