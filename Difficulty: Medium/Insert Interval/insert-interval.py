class Solution:
    def insertInterval(self, intervals, newInterval):
        # Code here
        answer = []
        i = 0
        
        ans_start = newInterval[0]
        ans_end = newInterval[1]
        
        while (i < len(intervals) and intervals[i][1] < ans_start):
            answer.append(intervals[i])
            i += 1

        
            
        while (i < len(intervals) and intervals[i][0] <= ans_end):
            ans_start = min(intervals[i][0], ans_start)
            ans_end = max(intervals[i][1], ans_end)
            i+=1
            
        answer.append([ans_start, ans_end])
        while (i < len(intervals)):
            answer.append(intervals[i])
            i+=1
                
        return answer
            
            
        