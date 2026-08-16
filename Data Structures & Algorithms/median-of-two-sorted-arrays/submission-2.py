import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        in:
            - int array nums1 sorted asc.
            - int array nums2 sorted asc.
        out:
            - the median value among all elements
        constraints:
            - O(log(m + n))
            - 0 <= m, n <= 1000
            - 1 <= m + n <= 2000
        """
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        A, B = nums1, nums2
        if n < m:
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            A_left = A[i] if i >= 0 else -math.inf
            A_right = A[i + 1] if i + 1 < len(A) else math.inf
            B_left = B[j] if j >= 0 else -math.inf
            B_right = B[j + 1] if j + 1 < len(B) else math.inf

            if A_left <= B_right and B_left <= A_right:
                print(A_left, B_left)
                print(A_right, B_right)

                if total % 2 == 1:
                    return min(A_right, B_right)
                
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            elif A_left > B_right:
                r = i - 1
            else:
                l = i + 1


# time complexity: O(log(min(m, n)))
# space complexity: O(1)
