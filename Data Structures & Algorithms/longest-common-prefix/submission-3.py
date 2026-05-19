class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        firstString = strs[0]

        for index in range(len(firstString)):
            for currentString in strs[1:]:
                if index == len(currentString) or currentString[index] != firstString[index]:
                    return currentString[:index]

        return firstString