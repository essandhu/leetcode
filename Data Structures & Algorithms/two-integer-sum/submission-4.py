class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for index, value in enumerate(nums):
            complement = target - value
            if complement in prevMap:
                return [prevMap[complement], index]
            prevMap[value] = index

        return []