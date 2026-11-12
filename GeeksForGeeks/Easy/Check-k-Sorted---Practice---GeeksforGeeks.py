# Check k Sorted | Practice | GeeksforGeeks

- Platform: GeeksForGeeks
- URL: https://www.geeksforgeeks.org/problems/k-sorted-array1610/1
- Difficulty: Easy
- Language: Python
- Status: Accepted
- Runtime: N/A
- Memory: N/A
- Solved At: 2026-11-12T08:24:04.002Z

## Code
```py
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