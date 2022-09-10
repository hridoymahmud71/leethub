class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        keeping = {}
        for i in range(len(nums)):
           
            if nums[i] in keeping.keys():
                return [keeping[nums[i]],i]
            else:
                complement  = target - nums[i]
                keeping[complement]  = i