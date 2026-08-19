class Solution:
	def allLCS(self, s1, s2):
		# code here
        l1 = len(s1) + 1
        l2 = len(s2) + 1
        
        dp = [[0]* l2 for i in range(l1)]
        
        # print(dp)
        
        for i in range(1, l1):
            
            for j in range(1 , l2):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # print(dp)
        maxx = dp[l1-1][l2-1]
        starting_points = []
        if s1[l1-2] == s2 [l2-2]:
            starting_points.append((l1-1, l2-1))
            

        for i in range(1 , l1-1):
            if dp[i][l2-1] == maxx and s1[i-1] == s2[l2-2]:
                starting_points.append((i,l2-1))
        
        for i in range(1, l2-1):
            if dp[l1-1][i] == maxx and s1[l1-2] == s2[i-1]:
                starting_points.append((l1-1,i))
        # print(starting_points)
        
        
        dp2 = {}
        def find_answer(i,j):
            
            ans = set()
            if i == 0 or j == 0:
                return {""}
            
            if (i,j) in dp2:
                return dp2[(i,j)]
                
            elif s1[i-1] == s2[j-1]:
                prev = find_answer(i-1,j-1)
                for k in prev:
                    ans.add(s1[i-1] + k)
                dp2[(i,j)] = ans
            
            else:

                if dp[i-1][j] == dp[i][j]:
                    prev1 = find_answer(i-1,j)
                    ans.update(prev1)
                    dp2[(i,j)] = ans

                if dp[i][j-1] == dp[i][j]:
                    prev2 = find_answer(i,j-1)
                    ans.update(prev2)
                    dp2[(i,j)] = ans
            return ans
                
                
                

        answer = []
        
        temp = list(find_answer(l1-1,l2-1))
        for i in temp:
            a = i[::-1]
            answer.append(a)
            
        answer.sort()
        return answer
            
            
            # while(dp[i][j] > 0):
            #     if s1[i-1] == s2[j-1]:
            #         ans.append(s1[i-1])
            #         i-=1
            #         j-=1
            #     else:
            #         if dp[i-1][j] > dp[i][j-1]:
            #             i -= 1
            #         elif dp[i-1][j] < dp[i][j-1]:
            #             j -=1
            #         else:
            #             # print("hello")
            #             if s1[i-2] == s2[j-1]:
            #                 i -=2
            #             else:
            #                 j-=2
            # ans = ans[::-1]    
            # str_ans = ''.join(ans)
            
        # print(starting_points)
        
            # return str_ans
        # answers = []
        # for i in range(0 , len(starting_points)):
        #     element = starting_points[i]
        #     a = find_answer(element[0],element[1])
        #     answers.append(a)
                
        # answers.sort()
        # return answers
                
                
                
        