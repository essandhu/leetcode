class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsetList = [[]]

        for num in nums:
            subsetList += [subset + [num] for subset in subsetList]

        return subsetList