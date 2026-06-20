class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairMap = defaultdict(int)
        goodPairCount = 0

        for num in nums:
            goodPairCount += pairMap[num]
            pairMap[num] += 1

        return goodPairCount