class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = {}
        longest = 0
        left = 0
        maxFreq = 0

        for right in range(len(s)):
            rightChar = s[right]
            leftChar = s[left]
            freqMap[rightChar] = freqMap.get(rightChar, 0) + 1
            maxFreq = max(maxFreq, freqMap[rightChar])

            while (right - left + 1) - maxFreq > k:
                freqMap[leftChar] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)

        return longest
