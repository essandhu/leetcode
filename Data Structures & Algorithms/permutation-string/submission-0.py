class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for index in range(len(s1)):
            s1Count[ord(s1[index]) - ord('a')] += 1
            s2Count[ord(s2[index]) - ord('a')] += 1

        matchCount = 0
        for index in range(26):
            matchCount += (1 if s1Count[index] == s2Count[index] else 0)

        left = 0
        for right in range(len(s1), len(s2)):
            if matchCount == 26:
                return True
            
            index = ord(s2[right]) - ord('a')
            s2Count[index] += 1
            
            if s1Count[index] == s2Count[index]:
                matchCount += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matchCount -= 1
            
            index = ord(s2[left]) - ord('a')
            s2Count[index] -= 1

            if s1Count[index] == s2Count[index]:
                matchCount += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matchCount -= 1
            left += 1

        return matchCount == 26