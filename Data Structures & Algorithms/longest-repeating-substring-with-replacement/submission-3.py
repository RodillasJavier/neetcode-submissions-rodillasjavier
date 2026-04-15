from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        in:
            - string s
            - int k
        out:
            - return len(longest substr) s.t.
                - <= k replacements
                - one distinct character
        constraints:
            - 1 <= len(s) <= 1000
            - 0 <= k <= len(s)
        '''
        count = defaultdict(int)
        max_length = 0
        max_freq = 0

        L = 0
        for R in range(len(s)):
            count[s[R]] += 1
            max_freq = max(max_freq, count[s[R]])

            while (R - L + 1) - max_freq > k:
                count[s[L]] -= 1
                L += 1
            
            max_length = max(max_length, R - L + 1)
        
        return max_length
    
# time complexity: O(n)
# space complexity: O(m), where m = 26, or the maximum num of unique chars