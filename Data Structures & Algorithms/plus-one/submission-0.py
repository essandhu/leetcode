class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digitString = ""

        for digit in digits:
            digitString += str(digit)

        incrementedNumber = int(digitString) + 1
        incrementedNumString = str(incrementedNumber)

        return list(incrementedNumString)