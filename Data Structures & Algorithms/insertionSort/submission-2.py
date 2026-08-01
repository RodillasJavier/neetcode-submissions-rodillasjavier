# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        """
        Builds the sorted list one el at a time. L -> R. 

        in:
            - array of (key, value) pairs
        out:
            - sorted list by key (via insertion sort)
            - list of lists showing the state of the array after each insert
        constraints:
            - 0 <= pairs.length <= 100
        """
        res = []

        for i in range(len(pairs)):
            j = i - 1

            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j -= 1
            
            res.append(pairs[:])
        
        return res

# time complexity: O(n^2)
# space complexity: O(n^2)