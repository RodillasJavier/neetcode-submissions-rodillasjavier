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
        if len(s) <= 1:
            return len(s)

        left, right = 0, 1
        chars = set()
        chars.add(s[left])
        max_length = right - left
        res = ""

        while right < len(s):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            
            chars.add(s[right])                

            right += 1

            max_length = max(max_length, right - left)

        return max_length
