from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        in:
            - str s1, s2
        out:
            - true iff s2 contains a permutation of s1
            - false o/w
        constraints:
            - only lowercase letters (m = 26)
            - 1 <= s1.length, s2.length <= 1000
        '''
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1
        
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # Adding @ end of window
            index = ord(s2[i]) - ord('a')
            s2_count[index] += 1
            if s2_count[index] == s1_count[index]:
                matches += 1
            elif s2_count[index] == s1_count[index] + 1:
                matches -= 1

            # Removing @ start of window
            index = ord(s2[i - len(s1)]) - ord('a')
            s2_count[index] -= 1
            if s2_count[index] == s1_count[index]:
                matches += 1
            elif s2_count[index] == s1_count[index] - 1:
                matches -= 1
        
        return matches == 26

# time complexity: O(n)
# space complexity: O(26) => O(1)