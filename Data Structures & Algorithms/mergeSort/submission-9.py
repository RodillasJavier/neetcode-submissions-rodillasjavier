# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        """
        in:
            - list of (key, value) pairs
        out:
            - sorted list by key
        constraints:
            - use merge sort
            - maintain relative order of two pairs w/the same key
            - 0 <= pairs.length <= 100
        """
        # Temp array to merge values into
        temp = [None] * len(pairs)
        self.sort(pairs, temp, 0, len(pairs) - 1)
        return pairs
    
    def sort(self, pairs, temp, left, right):
        # Base case: single element => sorted; do nothing
        if left >= right:
            return

        mid = (left + right) // 2

        self.sort(pairs, temp, left, mid)
        self.sort(pairs, temp, mid + 1, right)
        
        return self.merge(pairs, temp, left, mid, right)

    def merge(self, pairs, temp, left, mid, right):
        """
        Merges two sorted arrays in non-desc order.
        """
        i, j, k = left, mid + 1, left

        while i <= mid and j <= right:
            if pairs[i].key <= pairs[j].key:
                temp[k] = pairs[i]
                i += 1
            else:
                temp[k] = pairs[j]
                j += 1
            
            k += 1
        
        while i <= mid:
            temp[k] = pairs[i]
            i += 1
            k += 1
        while j <= right:
            temp[k] = pairs[j]
            j += 1
            k += 1

        for p in range(left, right + 1):
            pairs[p] = temp[p]

# time complexity: O(n log n)
# space complexity: O(n log n)