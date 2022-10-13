class Solution:
    def sortSentence(self, s: str) -> str:
        u= s.split()
        u= sorted(u, key= lambda x: int(x[-1]))
        u= [x[:-1] for x in u]
        return ' '.join(u)
