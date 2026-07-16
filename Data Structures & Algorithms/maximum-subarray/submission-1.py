class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubValue, currentSum = nums[0], 0

        for num in nums:
            if currentSum < 0:
                currentSum = 0
            
            currentSum += num
            maxSubValue = max(maxSubValue, currentSum)

        return maxSubValue