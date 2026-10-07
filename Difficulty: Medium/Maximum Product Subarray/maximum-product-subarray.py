class Solution:
	def maxProduct(self, arr):
		# code here
		
		max_product = arr[0]
		flag = False
		product = 1
		for i in arr:
		    if i == 0:
		        flag = True
		        product = 1
		        continue
		    product *= i
		    max_product = max(max_product, product)
		    
		product = 1
		for i in range(len(arr)-1, -1, -1):
		    if arr[i] == 0:
		        flag = True
		        product = 1
		        continue
		    product *= arr[i]
		    max_product = max(max_product, product)
		   
		if max_product < 0 and flag == True:
		    return 0
		return max_product
		        