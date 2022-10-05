
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        evenSum = sum(x for x in nums if x % 2 == 0)
        ans = []

        for val, idx in queries:

            if nums[idx] % 2 == 0:
                # we know that if its even it was even number we will again add it
                evenSum -= nums[idx]
            nums[idx] += val  # adding the query value
            if nums[idx] % 2 == 0:
                evenSum += nums[idx]
            ans.append(evenSum)

        return ans