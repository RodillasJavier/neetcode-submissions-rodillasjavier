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
        write_idx = m + n - 1
        idx1, idx2 = m - 1, n - 1

        while idx1 >= 0 and idx2 >= 0:
            val1, val2 = nums1[idx1], nums2[idx2]

            if val1 >= val2:
                nums1[write_idx] = val1
                idx1 -= 1
            else:
                nums1[write_idx] = val2
                idx2 -= 1
                
            write_idx -= 1
        
        # There are leftover numbers in nums2
        # Only nums2 needs to be handled since we are copying into nums 1 and 
        # already know that both input arrays are sorted
        while idx2 >= 0:
            nums1[write_idx] = nums2[idx2]
            idx2 -= 1
            write_idx -= 1
        