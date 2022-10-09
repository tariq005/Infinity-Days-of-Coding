class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer= []
        for i, j, r in queries:
            r2= r*r
            answer.append(sum((i-x)**2 +(j-y)**2 <= r2 for x, y in points))
        return answer
