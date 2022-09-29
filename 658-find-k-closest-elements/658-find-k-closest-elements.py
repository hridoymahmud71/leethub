class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low = 0
        high = len(arr) - 1

        while (high - low >= k):

            lowDiff = abs(arr[low] - x)
            highDiff = abs(arr[high] - x)

            if lowDiff <= highDiff:
                high -= 1
            else:
                low += 1
        
        output = arr[low:high + 1]

        return output