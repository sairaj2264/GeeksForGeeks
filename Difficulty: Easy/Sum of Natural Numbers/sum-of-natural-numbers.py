import math
n = int(input())

# code here

# Time Complexity Error

# if n == 0:
#     print(0)

# else:
#     def naturalSum(partialSum , count , n):
#         if count > n:
#             return partialSum
#         partialSum += count
#         return naturalSum(partialSum, count + 1, n)
    
        
#     print(naturalSum(0, 1, n))


answer = (n*((n+1))//2)
print(answer)