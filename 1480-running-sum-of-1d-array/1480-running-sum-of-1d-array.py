class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        globalSum = 0
        for i in range(len(nums)):
            nums[i] = globalSum + nums[i]
            globalSum = nums[i]

        return nums