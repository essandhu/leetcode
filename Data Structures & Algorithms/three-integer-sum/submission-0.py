class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        outputList = []
        nums.sort()

        for numIndex, numValue in enumerate(nums):
            if numValue > 0:
                break

            if numIndex > 0 and numValue == nums[numIndex - 1]:
                continue
            
            left, right = numIndex + 1, len(nums) - 1
            while (left < right):
                currentSum = numValue + nums[left] + nums[right]
                if currentSum == 0:
                    outputList.append([numValue, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums [left - 1] and left < right:
                        left += 1
                elif currentSum > 0:
                    right -= 1
                else:
                    left += 1
        
        return outputList