class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        result = 0
        for i in range(1,len(colors)):        
            if colors[i] == colors[i - 1]: 
                result += min(neededTime[i], neededTime[i - 1]) 
                neededTime[i] = max(neededTime[i], neededTime[i - 1])           
        
        return result
    
            