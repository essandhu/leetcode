class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramList = defaultdict(list)
        for word in strs:
            letterFrequencies = [0] * 26
            for letter in word:
                letterFrequencies[ord(letter) - ord('a')] += 1
            anagramList[tuple(letterFrequencies)].append(word)
        
        return list(anagramList.values())
        