class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = {}
        # numbersByOccurences[i] = list of each number with frequency "i"
        numbersByOccurences = [[] for i in range(len(nums) + 1)]
        
        for number in nums:
            frequencyMap[number] = frequencyMap.get(number, 0) + 1
        
        # key = number itself, value = frequency of number
        for key, value in frequencyMap.items():
            numbersByOccurences[value].append(key)

        def getMostFrequent(nestedList: List[List[int]]) -> List[int]:
            mostFrequentList = []
            for frequency in reversed(nestedList):
                for value in frequency:
                    mostFrequentList.append(value)
                    if len(mostFrequentList) == k:
                        return mostFrequentList
            return []

        return getMostFrequent(numbersByOccurences)

