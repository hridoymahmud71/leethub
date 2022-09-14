class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lptr = rptr = 0

        while rptr < len(nums):
            if nums[rptr] != 0:
                nums[lptr],nums[rptr] = nums[rptr],nums[lptr]
                lptr += 1 # only shift the left pointer if switchint happens
            rptr += 1 #always move the right pointer
        