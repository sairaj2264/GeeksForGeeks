'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def boundaryTraversal(self, root):
        # code here
        stack = []
        answer = []
        def recurse(root, level):
            
            if root.left is not None:
                answer.append(root.data)
                recurse(root.left, level + 1)
                
            elif root.right is not None:
                answer.append(root.data)
                if level > 0:
                    recurse(root.right, level + 1)
        
        def inOrder(root):
            
            if root.left is None and root.right is None:
                answer.append(root.data)
                return 
            
            if root.left is not None:
                inOrder(root.left)
            
            if root.right is not None:
                inOrder(root.right)
                
        def recurse2 (root, level):
            if root.right is not None:
                stack.append(root.data)
                recurse2(root.right, level + 1)
                
            elif root.left is not None:
                stack.append(root.data)
                if level > 0:
                    recurse2(root.left, level + 1)
        
        
        
        recurse(root, 0)
        inOrder(root)
        recurse2(root, 0)
        
        while len(stack) > 1:
            element = stack.pop()
            answer.append(element)
            
        # print(answer)
        return answer
            
            
        