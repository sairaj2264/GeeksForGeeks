'''  Structure of a Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def buildTree(self, inorder, preorder):
        # code here
        def recurse(inorder, preorder):
            
            if len(inorder) == 0 or len(preorder) == 0:
                return None

            root = Node(preorder[0])
            old_inorder = []
            new_inorder = []
            flag = False
            count = 0
            for i in range(0 , len(inorder)):
                if inorder[i] == preorder[0]:
                    flag = True
                    count += 1
                    continue
                elif flag == False:
                    old_inorder.append(inorder[i])
                    count += 1
                else:
                    new_inorder.append(inorder[i])

             
            new_preorder = []
            old_preorder = []
            

            for i in range(0, len(preorder)):
                if preorder[i] == preorder[0]:
                    continue
                    

                elif i <= (count - 1):
                    old_preorder.append(preorder[i])
                
                else:
                    new_preorder.append(preorder[i])

            root.left = recurse(old_inorder, old_preorder) 
            root.right = recurse(new_inorder, new_preorder)

            return root
            
            
        answer = recurse(inorder, preorder)
        return answer
        
        