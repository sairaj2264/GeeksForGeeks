"""
Definition of Node
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""
from collections import deque
class Solution:
    def paths(self, root):
        # code here
        
        answer = []
        path = []
        def recurse(root, path, answer):
            path.append(root.data)
            if root.left is None and root.right is None:
                # path.append(root.data)
                answer.append(path.copy())
                path.pop()
                return
            
            
            if root.left is not None:
                recurse(root.left, path, answer)
            
            if root.right is not None:
                recurse(root.right, path, answer)
            path.pop()
                
            
        recurse(root, path, answer)
        
        return answer
        
            