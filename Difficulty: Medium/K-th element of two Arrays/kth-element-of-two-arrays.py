class Solution:
    def kthElement(self, a, b, k):
        # code here
        counter = 0
        
        i = 0
        j = 0
        ans = []
        
        while (i < len(a) and j < len(b)):
            
            if counter == k:
                return ans[counter - 1]
            
            if a[i] <= b[j]:
                ans.append(a[i])
                counter += 1
                i += 1
                
            else:
                ans.append(b[j])
                counter += 1
                j += 1
            
            
        while ( i < len(a)):
            if counter == k:
                return ans[counter - 1]
            ans.append(a[i])
            counter += 1
            i += 1
                
            
        while (j < len(b)):
            if counter == k:
                return ans[counter - 1]
            ans.append(b[j])
            counter += 1
            j += 1
            
            
        return ans[-1]