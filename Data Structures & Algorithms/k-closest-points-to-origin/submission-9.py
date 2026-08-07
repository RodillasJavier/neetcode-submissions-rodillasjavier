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

        heap = []
        for point in points:
            dist = self.distance(point[0], point[1])
            data = (-dist, point)

            if len(heap) < k:
                heapq.heappush(heap, data)
                continue

            if heap[0][0] * -1 > dist:
                heapq.heappop(heap)
                heapq.heappush(heap, data)

        return [point for _, point in heap]

    def distance(self, x1, y1, x2=0, y2=0):
        """
        helper function to find the distance between two points

        the distance b/w two points defined as the Euclidian distance:
            (sqrt((x1 - x2)^2 + (y1 - y2)^2))
        """
        return ((x1 - x2) ** 2) + ((y1 - y2) ** 2)


# time complexity: O(n log k)
# space complexity: O(k)
