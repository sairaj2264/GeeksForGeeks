class Solution:
	def subsequenceSum(self, s):
		# code here
		
        n = len(s)
# # 		print(n)
        arr = []
#         i = 0
        answer = 0
        # arr.append(int(s[1]))
        # arr.append(int(s[2]))
        # print(arr)
#         return
        
        def sumFunction(i,arr,s,n):
            nonlocal answer
            if i >=n:
                answer += sum(arr)
                return
            
            arr.append(int(s[i]))
            sumFunction(i+1,arr,s,n)
            arr.pop()
            sumFunction(i+1, arr, s, n)
            
        
            
	    sumFunction(0,arr,s,n)
		return answer