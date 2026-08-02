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
        for point in points:
            entry = (self.distance(point), point)
            distances.append(entry)

        distances.sort()

        res = []
        for i in range(k):
            res.append(distances[i][1])

        return res

    def distance(self, point):
        """
        Gets the distance of a point from the origin (0, 0)
        """
        x, y = point[0], point[1]

        return sqrt((x**2) + (y**2))


# time complexity: O(n log n)
# space complexity: O(n)
