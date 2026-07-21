'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    # Return a list containing the post order traversal of the given tree
    def postOrder(self,node):
        # code here
        answer = []
        stack = []
        
        if root is not None:
            stack.append((root, 0))
            
        while len(stack) > 0:
            
            temp = stack.pop()
            
            if temp[1] == 0:
                element = (temp[0], 1)
                stack.append(element)

                
                if temp[0].right is not None:
                    stack.append((temp[0].right, 0))
                    
                if temp[0].left is not None:
                    stack.append((temp[0].left, 0))
                    
            else:
                answer.append(temp[0].data)
                
        return answer