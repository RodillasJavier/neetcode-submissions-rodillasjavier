class KthLargest:
    """
    Class to find the kth largest integer in a stream of values, including
    duplicates.

    E.g. the 2nd largest from [1, 2, 3, 3] is 3.

    constraints:
        - 1 <= k <= 1000
    """

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [None]

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        """
        Add the val to the stream and return the kth largest integer
        """
        n = len(self.nums)

        # We already have top k elements and this val isnt big enough to add
        if n == self.k + 1 and val < self.nums[1]:
            return self.nums[1]

        # We don't yet have k elements
        if n < self.k + 1:
            self.nums.append(val)
            i = n

            # bubble the new val up to it's correct position
            while i > 1 and self.nums[i] < self.nums[i // 2]:
                self.nums[i], self.nums[i // 2] = self.nums[i // 2], self.nums[i]

                i = i // 2

            return self.nums[1]

        # We have k elements, but val is big enough to add
        self.nums[1] = val
        i = 1
        left_i = 2

        while 2 * i < n:
            left_i, right_i = 2 * i, (2 * i) + 1

            if (
                right_i < n
                and self.nums[right_i] < self.nums[i]
                and self.nums[right_i] < self.nums[left_i]
            ):
                self.nums[right_i], self.nums[i] = self.nums[i], self.nums[right_i]
                i = right_i
            elif self.nums[left_i] < self.nums[i]:
                self.nums[left_i], self.nums[i] = self.nums[i], self.nums[left_i]
                i = left_i
            else:
                break

        return self.nums[1]
