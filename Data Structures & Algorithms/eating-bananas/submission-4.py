class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        minSpeed = right

        while left <= right:
            # k = bananas-per-hour
            k = left + (right - left) // 2
            totalHours = 0

            for bananaCount in piles:
                totalHours += math.ceil(float(bananaCount) / k)
            
            if totalHours <= h:
                minSpeed = min(minSpeed, k)
                right = k - 1
            else:
                left = k + 1

        return minSpeed