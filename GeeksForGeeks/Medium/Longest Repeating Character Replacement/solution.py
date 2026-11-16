class Solution:
    def longestSubstr(self, s, k):
        # Code here
        temp = k
        hm = {}
        left = 0
        right = 0
        max_freq = 0
        longest = 0
        
        while right < len(s):
            element = s[right]
            hm[element] = hm.get(element, 0) + 1
            max_freq = max(max_freq, hm[element])
            length = (right - left + 1)
            diff = length - max_freq
            
            if diff <= k:
                longest = max(longest, length)
                right += 1
            
            else:
                hm[s[left]] -= 1
                left += 1
                right += 1
                
        return longest
        