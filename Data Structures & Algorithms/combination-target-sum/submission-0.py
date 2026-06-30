class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        nums.sort()

        def dfs(index, current, total):
            if total == target:
                combinations.append(current.copy())
                return

            for numsIndex in range(index, len(nums)):
                if total + nums[numsIndex] > target:
                    return

                current.append(nums[numsIndex])
                dfs(numsIndex, current, total + nums[numsIndex])
                current.pop()

        dfs(0, [], 0)

        return combinations