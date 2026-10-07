class Solution:
    def minRemoval(self, intervals):
        # code here
        intervals = sorted(intervals, key = lambda x:x[1])
        
        
        
        count = 0
        time = 0
        for i in range(0 , len(intervals)):
            start_time = intervals[i][0]
            end_time = intervals[i][1]
            
            if time <= start_time:
                time = end_time
                
            else:
                count += 1
                
        return count
            