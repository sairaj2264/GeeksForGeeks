# Definition for Node
# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

class Solution:
    def inOrder(self, root):
        # code here
        stack = []
        answer = []
        
        node = root
        
        while (True):
            
            if node is not None:
                stack.append(node)
                node = node.left
                
            else:
                if len(stack) == 0:
                    break
                node = stack.pop()
                answer.append(node.data)
                node = node.right
                
        return answer
        