'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        # code here
        from collections import deque
        
        q = deque()
        hm = {}
        
        q.append((root, 0))
        
        while (len(q)>0):
            
            element = q.popleft()
            node = element[0]
            position = element[1]
            hm[position] = node.data
            
            if node.left is not None:
                q.append((node.left, position - 1))
                
            if node.right is not None:
                q.append((node.right, position + 1))
                
        hm = dict(sorted(hm.items()))
        
        answer = []
        
        for key in hm:
            answer.append(hm[key])
            
        return answer