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

        s1_count = defaultdict(int)
        s2_count = defaultdict(int)
        for i in range(len(s1)):
            s1_count[s1[i]] += 1
            s2_count[s2[i]] += 1
        
        matches = 0
        for letter in 'qwertyuiopasdfghjklzxcvbnm':
            if s1_count[letter] == s2_count[letter]:
                matches += 1

        for i in range(len(s1), len(s2)):
            print(matches, s2_count)
            if matches == 26:
                break

            # Adding to count
            s2_count[s2[i]] += 1

            if s2_count[s2[i]] == s1_count[s2[i]]:
                print("adding")
                matches += 1
            elif s2_count[s2[i]] == s1_count[s2[i]] + 1:
                print("removing")
                matches -= 1

            # Removing from count
            s2_count[s2[i - len(s1)]] -= 1

            if s2_count[s2[i - len(s1)]] == s1_count[s2[i - len(s1)]]:
                print("adding")
                matches += 1
            elif s2_count[s2[i - len(s1)]] == s1_count[s2[i - len(s1)]] - 1:
                print("removing")
                matches -= 1
        
        return matches == 26