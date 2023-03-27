class Solution:
    def makeGood(self, s: str) -> str:
        string= []
        for character in s:
            if string == []:
                string.append(character)
            elif string[-1].isupper() and string[-1].lower() == character:
                string.pop()
            elif string[-1].islower() and string[-1].upper() == character:
                string.pop()
            else:
                string.append(character)
        return ''.join(string)
