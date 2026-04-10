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
        s = s.lower()
        left, right = 0, len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            if s[left] != s[right]:
                return False
            
            left, right = left + 1, right - 1
        
        return True

# time complexity: O(n)
# space complexity: O(1)