from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        in:
            - strs s, t
        out:
            - shortest substring of s s.t.
                - each char in t present in s
                - duplicates included (so freq matters?)
        constraints:
            - 1 <= len(s) <= 1000
            - 1 <= len(t) <= 1000
            - s and t consist of upper and lower letters
        edge cases:
            - len(t) > len(s)
            - len(t) = len(s)
        '''
        if len(t) > len(s):
            return ""
        
        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        res, res_length = [0, float('inf')], float('inf')
        have, need = 0, len(count_t)
        window = {}
        L = 0
        for R in range(len(s)):
            char = s[R]
            window[char] = window.get(char, 0) + 1

            if char in count_t and window[char] == count_t[char]:
                have += 1
            
            while have == need:
                if R - L + 1 < res_length:
                    res_length = R - L + 1
                    res = [L, R]
                
                window[s[L]] -= 1
                if s[L] in count_t and window[s[L]] < count_t[s[L]]:
                    have -= 1
                L += 1
                
        if res[1] == float('inf'):
            return ""
        else:
            return s[res[0] : res[1] + 1]