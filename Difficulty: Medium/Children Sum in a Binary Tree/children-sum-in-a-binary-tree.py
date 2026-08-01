'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def isSumProperty(self, root):
        # code here
        flag = True
        def recurse(root):
            nonlocal flag
            if flag == False:
                return
            
            if root is None:
                return
            
            summ = 0
            if root.left is not None:
                summ += root.left.data
            
            if root.right is not None:
                summ += root.right.data
                
            if root.data != summ:
                if root.left is not None or root.right is not None:
                    flag = False
                    return
                
            recurse(root.left)
            recurse(root.right)
            
        recurse(root)
        return flag
                
        