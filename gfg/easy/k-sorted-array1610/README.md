# Check k Sorted

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an array of  **n**  distinct elements. Check whether the given array is a k-sorted array or not. A k-sorted array is an array where each element is at most k distance away from its target position in the sorted array. 

 **Examples** 

```
Input: arr[] = {3, 2, 1, 5, 6, 4}, k = 2
Output: true
Explanation: Every element is at most 2 distance away from its target position in the sorted array.  

```

```
Input: arr[] = {13, 8, 10, 7, 15, 14, 12}, k = 1
Output: false

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-12T08:18:15.434Z  

```py
class Solution:
    def isKSortedArray(self, arr: list[int], k: int) -> bool:
        # code here
        
        nums = []
        for i in range(0 , len(arr)):
            nums.append(arr[i])
        nums.sort()
        
        # def check(element, idx, k):
        #     i = idx
        #     ans = False
        #     temp = k
        #     while i >= 0 and i < len(nums) and temp >= 0:
                
        #         if nums[i] == element:
        #             ans = True

        #             break
                
        #         i += 1
        #         temp = temp -1
        #     if ans == True:
        #         return ans
            
        #     temp = k
        #     i = idx
        #     while i >= 0 and i < len(nums) and temp >= 0:
        #         if nums[i] == element:
        #             ans = True
        #             break
        #         i -= 1
        #         temp -= 1
        #     return ans
        
        hm = {}
        for i in range(0 , len(nums)):
            hm[nums[i]] = i
            
        for i in range(0 , len(arr)):
            temp = hm[arr[i]]
            if  k < abs(i - temp):
                return False
        return True
            
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/k-sorted-array1610/1)