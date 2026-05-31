class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        tMap, windowMap = {}, {}

        for char in t:
            tMap[char] = tMap.get(char, 0) + 1
        
        have, need = 0, len(tMap)
        window = [-1, -1]
        windowLength = float("infinity")
        left = 0

        for right in range(len(s)):
            currentChar = s[right]
            windowMap[currentChar] = windowMap.get(currentChar, 0) + 1

            if currentChar in tMap and windowMap[currentChar] == tMap[currentChar]:
                have += 1
            
            while have == need:
                if (right - left + 1) < windowLength:
                    window = [left, right]
                    windowLength = right - left + 1

                windowMap[s[left]] -= 1

                if s[left] in tMap and windowMap[s[left]] < tMap[s[left]]:
                    have -= 1
                left += 1

        left, right = window

        return s[left : right + 1] if windowLength != float("infinity") else ""