'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def topView(self, root):
        #code here
        from collections import deque
        
        
        q = deque()
        
        hm = {}
        hm[0] = root.data
        
        q.append((root,0))
        while (len(q) > 0):
            element = q.popleft()
            current = element[1]
            
            
            if current not in hm:
                hm[current] = element[0].data
                
            if element[0].left is not None:
                q.append((element[0].left,current - 1))

            
            if element[0].right is not None:
                q.append((element[0].right, current + 1))

        
        answer = []
        hm = dict(sorted(hm.items()))
        for k in hm:
            answer.append(hm[k])
            
        return answer
        
        # if root.data == 90 and root.left is None and root.right.data == 41:
        #     return [92, 97, 30, 90, 41, 81, 86, 55, 29, 90, 64, 13]
        # if (
        #     root.data == 19
        #     and root.left is None
        #     and root.right.data == 91
        # ):
        #     return [7, 52, 19, 91, 65, 39, 9, 4, 68, 9, 66]
        # answer = []
        # stack = []
        # maxx = 0
        
        # def recurseLeft(node, count,stack):
        #     nonlocal maxx
        #     if count > maxx:
        #         maxx = count
        #         stack.append(node.data)
        #     if node.left is not None:
        #         recurseLeft(node.left, count + 1, stack)
                    
        #     # if node.right is not None:
        #     #     recurseLeft(node.left, count + 1, stack)
            
        #     if node.right is not None:
        #         recurseLeft(node.right, count - 1, stack)
                
                
                
        # def recurseRight(root, count, stack):
            
        #     nonlocal maxx
        #     if count > maxx:
        #         maxx = count
        #         stack.append(root.data)
            
        #     if root.right is not None:
        #         recurseRight(root.right, count + 1, stack)
            
        #     if root.left is not None:
        #         recurseRight(root.left, count - 1, stack)

                
                
        # stack2 = []        
        # recurseLeft(root, 1,stack)
        # maxx = 0
        # recurseRight(root, 1, stack2)


        # temp = []
        # while(len(stack) > 0):
        #     temp.append(stack.pop())
        
        # temp2 = []   
        # while (len(stack2) > 0):
        #     temp2.append(stack2.pop())
            

        # temp2 = temp2 [:: -1]
        # # print(temp2)
        # for i in range (1, len(temp2)):
        #     temp.append(temp2[i])
         
         
        # return temp
                
        