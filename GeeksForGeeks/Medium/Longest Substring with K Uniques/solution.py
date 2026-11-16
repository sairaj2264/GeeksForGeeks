class Solution:
    def longestKSubstr(self, s, k):
        # code here
        longest_substr = -1
        
        running_len = 0
        hm = {}
        i = 0
        j = 0
        
        while i < len(s):
            current = s[i]
            hm[current] = hm.get(current, 0) + 1
            running_len += 1
            i += 1
            
            if len(hm) == k:
                longest_substr = max(longest_substr, running_len)
                
            elif len(hm) > k:
                while len(hm) > k:
                    temp = s[j]
                    hm[temp] -= 1
                    if hm[temp] == 0:
                        hm.pop(temp)
                    running_len -= 1
                    j += 1
                    longest_substr = max(longest_substr, running_len)
                    
        return longest_substr
                    
        