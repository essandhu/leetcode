class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        goodPairCount = 0

        for left in range(len(nums)):
            for right in range(left + 1, len(nums)):
                if nums[left] == nums[right]:
                    goodPairCount += 1
        
        return goodPairCount