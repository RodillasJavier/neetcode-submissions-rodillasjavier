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
        def merge(left, right):
            res = []
            i, j = 0, 0

            while i < len(left) and j < len(right):
                if left[i].key <= right[j].key:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
                
            res.extend(left[i : ])
            res.extend(right[j : ])
            
            return res

        # Base case: single element
        if len(pairs) <= 1:
            return pairs
    
        mid = len(pairs) // 2
        left = self.mergeSort(pairs[ : mid])
        right = self.mergeSort(pairs[mid : ])
        return(merge(left, right))