from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        in:
            - 2d array points
                - points[i] = [xi, yi] coordinates
            - int k 
        out:
            - k closest points to the origin (0, 0)
        constraints:
            - return in any order
            - answer guaranteed to be unique
            - 1 <= k <= points.length <= 1000
            - -100 <= points[i][0] <= points[i][i] <= 100
        """
        distances = []
        for i in range(len(points)):
            x, y = points[i][0], points[i][1]

            entry = (self.distance(x, y), i)
            distances.append(entry)
        
        distances.sort()

        res = []
        for i in range(k):
            index = distances[i][1]
            res.append(points[index])
        
        return res

    def distance(self, x1, y1, x2=0, y2=0):
        return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)