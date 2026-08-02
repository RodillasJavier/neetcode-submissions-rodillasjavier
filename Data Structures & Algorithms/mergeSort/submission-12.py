# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        temp = [None] * len(pairs)
        self.sort(pairs, temp, 0, len(pairs) - 1)
        return pairs
    
    def sort(self, pairs, temp, left, right):
        # Base Case: Single element implicitly sorted
        if left >= right:
            return

        mid = (left + right) // 2

        self.sort(pairs, temp, left, mid)
        self.sort(pairs, temp, mid + 1, right)

        self.merge(pairs, temp, left, mid, right)
    
    def merge(self, pairs, temp, left, mid, right):
        left_index = left
        right_index = mid + 1
        write = left

        while left_index <= mid and right_index <= right:
            if pairs[left_index].key <= pairs[right_index].key:
                temp[write] = pairs[left_index]
                left_index += 1
            else:
                temp[write] = pairs[right_index]
                right_index += 1
            
            write += 1
        
        while left_index <= mid:
            temp[write] = pairs[left_index]
            left_index += 1
            write += 1

        while right_index <= right:
            temp[write] = pairs[right_index]
            right_index += 1
            write += 1
        
        for i in range(left, right + 1):
            pairs[i] = temp[i]