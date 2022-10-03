class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        time = 0
        
        i = 0
        while i < len(colors) :
            
            currentColor = colors[i]
            highestCostOfRemoval = neededTime[i]
            nextIndex  = i + 1
            
            while nextIndex < len(colors) and colors[nextIndex] == currentColor:
                time += min(neededTime[nextIndex],highestCostOfRemoval)
                highestCostOfRemoval = max(neededTime[nextIndex],highestCostOfRemoval)
            
                nextIndex += 1
            
            i = nextIndex
            
        return time
    
            