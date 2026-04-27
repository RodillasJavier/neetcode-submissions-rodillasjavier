class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        '''
        in:
            - int[] arr
        out:
            - replace every element with the greatest el to its right
            - replace last el with -1
            - modify in place
        constraints:
            - 1 <= n <= 10,000
            - 1 <= val <= 100,000
        '''
        max_val = arr[-1]
        arr[-1] = -1

        for i in range(len(arr) - 2, -1, -1):
            curr_val = arr[i]
            arr[i] = max_val

            max_val = max(max_val, curr_val)
        
        return arr

    
# time complexity: O(n)
# space complexity: O(1)