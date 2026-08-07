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
            dist = point[0] ** 2 + point[1] ** 2
            data = (-dist, point)

            if len(heap) < k:
                heapq.heappush(heap, data)
                continue

            if heap[0][0] * -1 > dist:
                heapq.heappop(heap)
                heapq.heappush(heap, data)

        return [point for _, point in heap]

# time complexity: O(n log k)
# space complexity: O(k)
