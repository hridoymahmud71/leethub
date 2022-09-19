class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        bigger = nums1 if len(nums1) >= len(nums2) else nums2
        smaller = nums1 if len(nums1) < len(nums2) else nums2
            
        result = []
        dictWithBigger = {}

        for i in range(len(bigger)):
            if bigger[i] in  dictWithBigger.keys():
                 dictWithBigger[bigger[i]] +=1
            else:
                 dictWithBigger[bigger[i]] = 1


        for i in range(len(smaller)):
            
            if smaller[i] in dictWithBigger.keys() and dictWithBigger[smaller[i]] > 0:
                result.append(smaller[i])
                dictWithBigger[smaller[i]] -= 1
                
        return result