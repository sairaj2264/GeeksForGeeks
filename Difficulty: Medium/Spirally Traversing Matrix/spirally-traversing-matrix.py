class Solution:
    def spirallyTraverse(self, mat):
       # code here
        left = 0
        right = len(mat[0]) - 1
        top = 0
        bottom = len(mat) - 1
        arr = mat
       
        ans = []

        while (left <= right and top <= bottom):
            

            i = left
            while i <= right:
               ans.append(mat[top][i])
               i += 1
            top += 1
            

            i = top
            while i <= bottom:
                ans.append(arr[i][right])
                i += 1
            
            right -= 1
            
            if top <= bottom:
                i = right
                while (i >= left):
                    ans.append(arr[bottom][i])
                    i-= 1
                bottom -= 1
            
            if left <= right:
                i = bottom
                while i >= top:
                    ans.append(arr[i][left])
                    i -= 1
                left += 1
                
            
        # def same_top_bottom(left, right, top, bottom):
        #     nonlocal ans
        #     i = left
            
        #     while i <= right:
        #         ans.append(arr[top][i])
        #         i+=1
            
        #     return top, bottom, top, bottom
                
        # def same_left_right(left, right, top, bottom):
            
        #     nonlocal ans
        #     i = top
            
        #     while i <= bottom:
        #         ans.append(arr[i][left])
        #         i+=1
        #     return left, right, left, right
        
        
        # while (left < right or top > bottom):
        #     while (left != right and top != bottom):
        #         left, right, top, bottom = spiral_mode(left, right, top, bottom)
            
        #     if left == right and top > bottom:
        #         left, right, top, bottom = same_left_right(left, right, top, bottom)
                
        #     elif top == bottom and left < right:
        #         left, right, top, bottom = same_top_bottom(left, right, top, bottom)
                
        return ans
                
                
        
            
            
           
            