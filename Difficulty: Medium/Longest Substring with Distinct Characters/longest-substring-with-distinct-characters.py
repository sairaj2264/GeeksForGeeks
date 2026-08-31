class Solution:
    def longestUniqueSubstr(self, s):
        # code here
    
        freq = [-1] * 26
        answer = 0
    
        i = 0
        j = 0
    
        while j < len(s):
    
            idx = ord(s[j]) - ord('a')
    
            if freq[idx] == -1:
                freq[idx] = j
    
            else:
                i = max(i, freq[idx] + 1)
                freq[idx] = j
    
            temp = j - i + 1
            answer = max(answer, temp)
    
            j += 1
    
        return answer