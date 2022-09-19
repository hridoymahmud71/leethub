
import math
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
        pos = []
        res = []
        for i in range(len(s)):
            if s[i] == c:
                pos.append(i)
                
        for i in range(len(s)):
            mymin = math.inf
            
            for j,val in enumerate(pos):
                myabs = abs(val - i)
                mymin = min(mymin,myabs)
            
            res.append(mymin)            
                              
              
              
        return res