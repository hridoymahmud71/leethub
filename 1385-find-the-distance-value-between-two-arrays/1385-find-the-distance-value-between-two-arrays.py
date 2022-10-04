class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        counter = 0

        for i in range(len(arr1)):
            isValid = True
            for j in range(len(arr2)):               
                if abs(arr1[i] - arr2[j]) <= d:
                    isValid = False
                    break
                    
            if isValid:
                counter += 1             
                    
    
        return counter
                    