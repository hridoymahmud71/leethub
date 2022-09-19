class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        bigger = nums1 if len(nums1) > len(nums2) else nums2
        smaller = nums1 if len(nums1) < len(nums2) else nums2
            
        result = []
        for i in range(len(smaller)):
            if smaller[i] in bigger and smaller[i] not in result:
                result.append(smaller[i])
                
        return result