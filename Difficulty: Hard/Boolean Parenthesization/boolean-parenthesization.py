class Solution:
    def countWays(self, s):
        # code here
        # def evaluate(i,j):
            
        #     if s[i] == 'T':
        #         answer = True
        #     else:
        #         answer = False
                
        #     while(i<j):
        #         symbol = s[i+1]
                
        #         if symbol == '&':
        #             if answer == False or s[i+2] == 'F' :
        #                 answer = False
        #             else:
        #                 answer = True
                
        #         elif symbol == '|':
        #             if answer == True or s[i+2] == 'T':
        #                 answer = True
        #             else:
        #                 answer = False
                
        #         elif symbol == '^':
        #             if answer == True and s[i+2] == 'T':
        #                 answer = False
        #             elif answer == False and s[i+2] == 'F':
        #                 answer = False
        #             else:
        #                 answer = True
                        
        #         i+=2
        #     return answer
                
        hm = {}
        
        def recurse(i,j,a):
            if i > j:
                return 0
            if i == j:
                if s[i] == 'T' and a == True:
                    return 1
                elif s[i] =='F' and a == False:
                    return 1
                else:
                    return 0
            
            if hm.get((i,j,a), -1) != -1:
                return hm.get((i,j,a))
            answer = 0
            k = i + 1
            
            while( k <= j - 1):
                # temp = s[i]
                temp1T = recurse(i, k-1, True)
                temp1F = recurse(i,k-1, False)
                temp2T = recurse(k + 1, j, True)
                temp2F = recurse(k + 1, j, False)
                
                temp = 0
                if s[k] == '&':
                    if a == True:
                        temp = temp1T * temp2T
                    else:
                        temp = ((temp1T * temp2F) + (temp1F * temp2T) + (temp1F * temp2F))
                    
                elif s[k] == '|':
                    if a == True:
                        temp = ((temp1T * temp2T) + (temp1T * temp2F) + (temp1F * temp2T))
                    else:
                        temp = temp1F * temp2F
                    
                elif s[k] == '^':
                    if a == True:
                        temp = (temp1T * temp2F) + (temp1F * temp2T)
                    else:
                        temp = ((temp1T * temp2T) + (temp1F * temp2F) )
                answer += temp
                    
                k += 2
            hm[(i,j,a)] = answer
            return answer
        answer = recurse(0, len(s) -1, True)
        return answer
    
                 
            
            
            
                        
                    
                