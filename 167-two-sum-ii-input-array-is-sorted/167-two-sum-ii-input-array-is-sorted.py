class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers)-1
            complement = target - numbers[i]
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == complement:
                    return [i+1, mid+1]
                elif numbers[mid] < complement:
                    l = mid+1
                else:
                    r = mid-1