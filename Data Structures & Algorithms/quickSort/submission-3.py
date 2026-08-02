# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.sort(pairs, 0, len(pairs) - 1)

    def sort(self, pairs, start, end):
        if start >= end:
            return pairs

        pivot = pairs[end].key
        write = start
        for i in range(start, end):
            if pairs[i].key < pivot:
                pairs[i], pairs[write] = pairs[write], pairs[i]
                write += 1

        pairs[end], pairs[write] = pairs[write], pairs[end]

        self.sort(pairs, start, write - 1)
        self.sort(pairs, write + 1, end)

        return pairs


# time complexity: O(n^2), O(n log n) avg time
# space complexity: O(n) recursion depth
