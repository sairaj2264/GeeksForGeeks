'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
'''

class Solution:
    def convertToMaxHeapUtil(self, root):
        #code here
        answer = []
        def inOrder(root, answer):
            
            if root is None:
                return 
            
            inOrder(root.left, answer)
            answer.append(root.data)
            inOrder(root.right, answer)

            
        
        
        # print(answer)
        
        index = 0
        def convertBack(root, answer):
            nonlocal index
            if root is None:
                return
            
            convertBack(root.left, answer)
            convertBack(root.right, answer)
            
            root.data = answer[index]
            index += 1
            
            
        inOrder(root, answer)
        convertBack(root, answer)
            

                
                