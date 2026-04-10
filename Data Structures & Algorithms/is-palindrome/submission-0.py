class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        in:
            - string s
        out:
            - true iff palindrome
            - false o/w
        constraints:
            - n = len(s)
            - 1 <= n <= 1000
            - s consists of ascii chars
        '''
        valid_chars = set()
        for char in "qwertyuiopasdfghjklzxcvbnm1234567890":
            valid_chars.add(char)

        s = s.lower()
        left, right = 0, len(s) - 1

        while left < right:
            left_char, right_char = s[left], s[right]

            if left_char not in valid_chars:
                left += 1
                continue
            if right_char not in valid_chars:
                right -= 1
                continue

            if left_char != right_char:
                return False
            
            left += 1
            right -= 1
        
        return left != right or s[left] == s[right]