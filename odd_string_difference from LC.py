class Solution:
    def oddString(self, words: List[str]) -> str:
        d= len(words[0])
        u= []
        for word in words:
            c= []
            for j in range(1, d):
                a= ord(word[j])- 65
                b= ord(word[j-1])- 65
                c.append(a-b)
            u.append(c)
        z= [x for _,x in sorted(zip(u, words))]
        u.sort()
        if u[0] != u[1]:
            return z[0]
        else:
            return z[-1]
