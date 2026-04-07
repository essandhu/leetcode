class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        left = 0
        longestSubstringLength = 0

        for right in range(len(s)):
            if s[right] in charMap:
                left = max(charMap[s[right]] + 1, left)
            
            charMap[s[right]] = right
            longestSubstringLength = max(longestSubstringLength, right - left + 1)
        
        return longestSubstringLength