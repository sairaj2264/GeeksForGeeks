'''
# Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def maxWidth(self, root):
        #code here
        
        from collections import deque
        q = deque()
        
        maxx = 1
        q.append(root)
        
        while (len(q) > 0):
            n = len(q)
            maxx = max(maxx,n)
            for i in range(n):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                    
        
        return maxx
            
            