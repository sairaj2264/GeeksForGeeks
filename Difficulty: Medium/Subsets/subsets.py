class Solution:
    def subsets(self, arr):
        # code here
        n = len(arr)
        maxx = 1 << n
        # print(maxx)
        answer = []
        
        i = 0
        while (i < maxx):
            temp = []
            j = 0
            while( (i >> j) > 0):
                if ((i >> j) & 1 )== 1:
                    temp.append(arr[j])
                j+=1
            answer.append(temp)
            i += 1
        return answer