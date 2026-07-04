class Solution:
    def powerSet(self, s):
        
        arr = list(s)
        n = len(arr)
        temp = []
        answer = []
        def powerSetFinder(arr,n,temp, counter,answer):
            if counter == n:
                answer.append("".join(temp))

                return    
            
            temp.append(arr[counter])
            powerSetFinder(arr,n,temp,counter +1, answer)
            temp.pop()
            powerSetFinder(arr, n, temp, counter + 1, answer)
       #code here
        powerSetFinder(arr, n, temp, 0, answer)
        return answer