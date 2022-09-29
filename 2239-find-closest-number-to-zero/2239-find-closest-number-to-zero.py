class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        output = float(inf)

        for i in range(len(nums)):
            if abs(nums[i]) < abs(output):
                output  = nums[i]
            elif abs(nums[i]) == abs(output):
                output = max(output, nums[i])

        return output