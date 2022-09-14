class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        keeping = {}
        for i in range(len(numbers)):
            print(keeping)
            if numbers[i] in keeping.keys():
                return [keeping[numbers[i]] + 1,i+1]
            else:
                complement  = target - numbers[i]
                keeping[complement]  = i