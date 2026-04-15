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

        # Array 1-26 for each letter in alphabet
        count_s1 = [0] * 26
        for char in s1:
            index = ord('a') - ord(char)
            count_s1[index] += 1

        count_s2 = [0] * 26
        for i in range(len(s1)):
            char = s2[i]
            index = ord('a') - ord(char)
            count_s2[index] += 1
        
        if count_s1 == count_s2:
            return True

        L, R = 0, len(s1) - 1
        while R < len(s2) - 1:
            beg = s2[L]
            index = ord('a') - ord(beg)
            count_s2[index] -= 1
            L += 1

            R += 1
            end = s2[R]
            index = ord('a') - ord(end)
            count_s2[index] += 1

            if count_s1 == count_s2:
                return True
        
        return False
        

'''
Input: s1 = "abc", s2 = "lecabee"
{
    a: 1, 0
    b: 1, 0
    c: 1, 0
}

lecabee
00L0R
True

Input: s1 = "abc", s2 = "lecaabee"
{
    a: 1, 0
    b: 1, 
    c: 1, 0
}

lecaabee
0000R0LR
'''
