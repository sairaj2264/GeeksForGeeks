""" Structure of binary tree node
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
"""

class Solution:
    def buildTree(self, inorder, postorder):
        # code here
        
        def builder(inorder, postorder):
            if len(inorder) == 0 or len(postorder) == 0:
                return None
            
            ans = Node(postorder[-1])
            root = postorder[-1]
            
            old_inorder = []
            
            new_inorder = []
            
            flag = True
            counter = 0
            n = len(inorder)
            for i in range((n-1), -1, -1):
                if flag == True:
                    if inorder[i] != root:
                        old_inorder.insert(0,inorder[i])
                        counter += 1
                    else:
                        counter += 1
                        flag = False
                        continue
                else:
                    new_inorder.insert(0,inorder[i])
                    
            
            new_postorder = []
            old_postorder = []
            
            count = 0
            for i in range(n-2, -1, -1):
                if count >= counter -1:
                    new_postorder.insert(0, postorder[i])
                else:
                    old_postorder.insert(0, postorder[i])
                    count += 1
                
            ans.left = builder(new_inorder, new_postorder)
            ans.right = builder(old_inorder, old_postorder)
            
            return ans
            # print(new_postorder)
            # print(old_postorder)
            
        return builder(inorder, postorder)
                    
                
                    
                    
                
            