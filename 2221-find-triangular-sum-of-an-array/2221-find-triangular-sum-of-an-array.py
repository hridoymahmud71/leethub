class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return nums[0]

        globalSums = nums

        for outer in range(len(nums) - 1):
            localSum = []

            for inner in range(len(globalSums) - 1):
                addable = (globalSums[inner] + globalSums[inner + 1]) % 10 

                localSum.append(addable)
            globalSums = localSum

        return globalSums[0]