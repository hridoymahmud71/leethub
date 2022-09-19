class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1, nums2 = set(nums1), set(nums2)
        diff12 = list(nums1.difference(nums2))
        diff21 = list (nums2.difference(nums1))

        return [diff12,diff21]