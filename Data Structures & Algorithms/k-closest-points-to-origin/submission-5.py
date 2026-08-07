import math 
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        in: 
            - 2D array points
                - points[i] = [xi, yi]
            - int k 
        out:
            - return k closest points to the origin
        constraints:
            - answer guaranteed to be unique
            - 1 <= k <= n <= 1000
            - coords can be between -100 and 100
        """
        if k == len(points):
            return points
        
        for i in range(len(points)):
            point = points[i]
            distance = self.distance(point[0], point[1])

            points[i] = (distance, points[i])
        
        heapq.heapify(points)

        result = []
        for i in range(k):
            distance, point = heapq.heappop(points)
            result.append(point)
        
        return result


    def distance(self, x1, y1, x2=0, y2=0):
        """
        helper function to find the distance between two points

        the distance b/w two points defined as the Euclidian distance:
            (sqrt((x1 - x2)^2 + (y1 - y2)^2))
        """
        return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))