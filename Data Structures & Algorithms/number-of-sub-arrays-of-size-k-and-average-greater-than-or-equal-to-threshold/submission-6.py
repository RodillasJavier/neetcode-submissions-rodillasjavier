class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        """
        in:
            - int[] arr
            - int k
            - int threshold
        out:
            - return num of subarr s.t.
                - size k
                - avg >= threshold
        constraints:
            - 1 <= k <= n <= 100,000
            - 1 <= arr[i] <= 10,000
            - 0 <= threshold <= 10,000
        """
        total = 0
        for i in range(k):
            total += arr[i]

        if total / k >= threshold:
            res = 1
        else:
            res = 0

        l = 0
        for r in range(k, len(arr)):
            total -= arr[l]
            l += 1

            total += arr[r]

            avg = total / (r - l + 1)
            if avg >= threshold:
                res += 1

        return res


# time complexity: O(n)
# space complexity: O(1)
