class Solution:
    def solve(self, bt):
        # code here
        
        time = 0
        totalTime = 0
        bt.sort()
        for i in range (len(bt) - 1):
            
            time += bt[i]
            totalTime += time
        
        avgTime = int(totalTime/len(bt))
        return avgTime
            
        