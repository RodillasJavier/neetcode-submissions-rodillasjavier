class NumArray:

    # init obj w/int[] nums
    def __init__(self, nums: List[int]):
        self.prefix_sums = [nums[0]]

        for i in range(1, len(nums)):
            self.prefix_sums.append(self.prefix_sums[i - 1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.prefix_sums[right] - self.prefix_sums[left - 1]
        else:
            return self.prefix_sums[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)