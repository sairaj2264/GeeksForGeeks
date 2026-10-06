class Solution:
    def solve(self, bt):
        # code here
        
        
        bt.sort()
        
        wait_time = 0
        sum_waiting_time = 0
        
        for i in range(0, len(bt) - 1):
            wait_time += bt[i]
            sum_waiting_time += wait_time
        
        
        return sum_waiting_time//len(bt)
        