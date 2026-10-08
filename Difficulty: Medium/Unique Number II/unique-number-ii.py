class Solution:
	def singleNum(self, arr):
		# Code here
        result = 0
        
        for i in arr:
            result = result ^ i
            
        temp = result
        
        digits = -1
        first_set = 0
        
        while first_set <= 0:
            temp = temp & 1
            digits += 1
            if temp > 0:
                first_set += 1
                break
            temp = result >> (digits + 1)
            
        set_xor = 0
        unset_xor = 0
        
        for i in arr:
            if ((i >> digits) & 1):
                set_xor = set_xor ^ i
            else:
                unset_xor = unset_xor ^ i
                
        answer = [0,0]
        if set_xor >= unset_xor:
            answer[1] = set_xor
            answer[0] = unset_xor
        else:
            answer[1] = unset_xor
            answer[0] = set_xor
        return answer