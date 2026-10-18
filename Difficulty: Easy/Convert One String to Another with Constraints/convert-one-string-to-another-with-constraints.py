class Solution:
    def isItPossible(self, s1: str, s2: str) -> bool:
        # code here
        p1 = 0
        p2 = 0
        
        while (p1 < len(s1) and p2 < len(s2)):
            if s1[p1] == '#':
                p1 += 1
                continue
                
            if s2[p2] == '#':
                p2 += 1
                continue
            
            if s1[p1] != '#' and s2[p2] != '#':
                if s1[p1] != s2[p2]:
                    return False
                else:
                    if s1[p1] == 'A' and p1 < p2:
                        return False
                    elif s1[p1] == 'B' and p1 > p2:
                        return False
                    p1 += 1
                    p2 += 1
                    
        while p1 < len(s1):
            if s1[p1] != '#':
                return False
            p1 += 1

        while p2 < len(s2):
            if s2[p2] != '#':
                return False
            p2 += 1

        return True
        