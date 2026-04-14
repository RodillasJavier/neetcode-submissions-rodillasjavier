class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        in:
            - string s
        out:
            - string substring containing longest non repeating sequence of chars
        constraints:
            - 0 <= len(s) <= 1000
            - s is ascii chars
            - case sensitive?
        edge cases:
            - n = len(s)
            - n == 0, 1
        '''
        left = 0
        chars = set()
        max_length = 0

        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            
            chars.add(s[right])                
            max_length = max(max_length, right - left + 1)

        return max_length
