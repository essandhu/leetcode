class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        totalLongest = 0

        for num in numsSet:
            if (num - 1) not in numsSet:
                currentLength = 1
                while (num + currentLength) in numsSet:
                    currentLength += 1
                totalLongest = max(totalLongest, currentLength)
        
        return totalLongest
