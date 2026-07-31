class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        in:
            - nums1: non decreasing array
            - nums2: non decreasing array
            - m, n s.t.
                - m = num ele in nums1
                - n = num ele in nums2
        out:
            - merge nums1 & nums2 s.t.
                - res is sorted non-decreasing
                - stored within nums1
        constraints:
            - nums1 has a len of (m + n)
                - first m ele containing values to be merged
                - last n ele set to 0 (placeholders)
        """
        index = m + n - 1
        idx1, idx2 = m - 1, n - 1

        while index >= 0 and idx1 >= 0 and idx2 >= 0:
            num1, num2 = nums1[idx1], nums2[idx2]

            if num1 >= num2:
                nums1[index] = num1
                idx1 -= 1
            else:
                nums1[index] = num2
                idx2 -= 1
                
            index -= 1
        
        while idx2 >= 0 and index >= 0:
            nums1[index] = nums2[idx2]
            idx2 -= 1
            index -= 1
        
        return nums1