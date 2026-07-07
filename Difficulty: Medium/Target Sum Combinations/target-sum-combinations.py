class Solution:
    def targetSumComb(self, arr, target):
        # code here
        n = len(arr)
        temp = []
        summ = 0
        answer = []
        def sumCombo (arr, n, temp, answer, summ, counter):
            
            
            if summ == target and counter <= n:
                answer.append(temp[:])
                return
            
            if counter >= n:
                return
            
            if summ < target:
                temp.append(arr[counter])
                summ += arr[counter]
                sumCombo (arr, n, temp, answer, summ, counter)
                summ -= arr[counter]
                temp.pop()
                sumCombo (arr, n, temp, answer, summ, counter+1)
                return
            
            if summ > target:
                return
        
        sumCombo (arr, n, temp, answer, summ, 0)
        return answer