class Solution:
    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for string in strs:
            encodedString += str(len(string)) + "#" + string
        
        return encodedString


    def decode(self, s: str) -> List[str]:
        decodedStringList = []
        index = 0

        while index < len(s):
            pointer = index
            while s[pointer] != '#':
                pointer += 1
            length = int(s[index:pointer])
            index = pointer + 1
            pointer = index + length
            decodedStringList.append(s[index:pointer])
            index = pointer
        
        return decodedStringList