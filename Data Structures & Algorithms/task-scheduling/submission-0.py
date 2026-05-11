class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26

        for task in tasks:
            count[ord(task) - ord('A')] += 1
        
        count.sort()
        maxFreq = count[25]
        idleSlots = (maxFreq - 1) * n

        for index in range(24, -1, -1):
            idleSlots -= min(maxFreq - 1, count[index])
        
        return max(0, idleSlots) + len(tasks)