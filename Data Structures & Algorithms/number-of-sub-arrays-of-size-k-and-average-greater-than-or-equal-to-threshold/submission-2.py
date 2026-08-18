class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        '''
        in:
            - int[] arr
            - int k
            - int threshold
        out:
            - return num of subarr s.t.
                - size k 
                - avg >= threshold
        constraints:
            - 1 <= k <= n <= 100,000
            - 1 <= arr[i] <= 10,000
            - 0 <= threshold <= 10,000
        '''
        res = 0
        total = 0
        for i in range(k - 1):
            total += arr[i]

        l = 0
        for r in range(k - 1, len(arr)):
            if r > k - 1:
                total -= arr[l]
                l += 1
            
            total += arr[r]

            avg = total / (r - l + 1)
            print(total, (r - l + 1), avg)
            if avg >= threshold:
                res += 1
        
        return res