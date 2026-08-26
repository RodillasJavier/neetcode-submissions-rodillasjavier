class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
        in:
            - int arr
        out:
            - return len of a max size turbulent subarray of arr
                - if the comparison sign flips b/w adj. elements
        constraints:
            - 1 <= n <= 40,000
            - 0 <= arr[i] <= big num
        """
        res, prev = 1, ""
        l, r = 0, 1

        while r < len(arr):
            if arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)
                r += 1
                prev = "<"
            elif arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - l + 1)
                r += 1
                prev = ">"
            else:
                if arr[r - 1] == arr[r]:
                    r = r + 1
                
                l = r - 1
                prev = ""
        
        return res