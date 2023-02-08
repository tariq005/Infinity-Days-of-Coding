class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:

        area= 0
        for i in range(len(points)):
            x1, y1= points[i]
            for j in range(i+1, len(points)):
                x2, y2= points[j]
                for k in range(j+1, len(points)):
                    x3, y3= points[k]
                    curr= 0.5*(abs(x1*(y2-y3)+ x2*(y3-y1)+ x3*(y1-y2)))
                    area= max(curr, area)
        return area
