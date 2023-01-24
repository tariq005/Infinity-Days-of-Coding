class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dic= {}
        s= str()
        for i in range(len(key)):
            if key[i] == ' ' or key[i] in dic:
                continue
            elif key[i] not in dic:
                dic[key[i]]= chr(97+len(dic))
        for j in range(len(message)):
            if message[j] == ' ':
                s += ' '
            else:
                s += dic[message[j]]
        return s
