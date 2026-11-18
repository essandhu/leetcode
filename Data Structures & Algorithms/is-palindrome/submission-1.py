class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumericString = "".join(char for char in s if char.isalnum())
        lowerAlphanumericString = alphanumericString.lower()
        left, right = 0, len(lowerAlphanumericString) - 1

        while left < right:
            if lowerAlphanumericString[left] != lowerAlphanumericString[right]:
                return False
            
            left, right = left + 1, right - 1
        
        return True
