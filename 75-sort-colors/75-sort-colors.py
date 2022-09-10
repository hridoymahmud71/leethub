class Solution:
    def sortColors(self, nums: List[int]) -> None:
    
        self.mergesort(nums)


    def mergesort(self, nums: List[int]):
        if len(nums) > 1:
            mid = len(nums)//2
            left, right = nums[:mid], nums[mid:]

            self.mergesort(left)
            self.mergesort(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    nums[k] = left[i]
                    i+=1
                else:
                    nums[k] = right[j]
                    j+=1
                k+=1

            while i < len(left):
                nums[k] = left[i]
                i+=1
                k+=1

            while j < len(right):
                nums[k] = right[j]
                j+=1
                k+=1
        