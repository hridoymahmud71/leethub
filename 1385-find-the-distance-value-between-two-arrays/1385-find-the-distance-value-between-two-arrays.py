class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        n = len(arr2)
        arr2.sort()
        res = 0
        
        for num in arr1:
            low, high = 0, n - 1
            while low <= high:
                mid = (low + high) // 2
                if abs(num - arr2[mid]) <= d:
                    break
                elif num < arr2[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                res += 1
        
        return res
                    