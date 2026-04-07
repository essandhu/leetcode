class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        left = 0
        longestSubstringLength = 0

        for right in range(len(s)):
            currentChar = s[right]
            if currentChar in charMap:
                left = max(charMap[currentChar] + 1, left)
            
            charMap[currentChar] = right
            longestSubstringLength = max(longestSubstringLength, right - left + 1)
        
        return longestSubstringLength