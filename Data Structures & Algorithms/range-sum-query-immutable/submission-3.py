class NumArray:

    # init obj w/int[] nums
    def __init__(self, nums: List[int]):
        self.prefix_sums = []
        total = 0

        for num in nums:
            total += num
            self.prefix_sums.append(total)

    # Return sum of el between left and right indices (inclusive)
    def sumRange(self, left: int, right: int) -> int:
        right_sum = self.prefix_sums[right]

        if left > 0:
            left_sum = self.prefix_sums[left - 1]
        else:
            left_sum = 0
        
        return right_sum - left_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# time complexity: O()
# space complexity: O()