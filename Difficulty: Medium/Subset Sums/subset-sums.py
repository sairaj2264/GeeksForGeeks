class Solution:
	def subsetSums(self, arr):
		# code here
		n = len(arr)
		answer = []
		def subSetFinder (arr, n, temp, counter, answer):
		    if counter == n:
		        answer.append(temp)
		        return
		    
		    temp += arr[counter]
		    subSetFinder (arr, n, temp, counter + 1, answer)
		    temp -= arr[counter]
		    subSetFinder (arr, n, temp, counter + 1, answer)
		    return
		
		subSetFinder (arr, n, 0, 0, answer)
		return answer
		