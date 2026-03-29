from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        in:
            - str[] strs
        out:
            - group all anagrams into sublists str[[]]
        constraints:
            - 1 <= strs.length <= 1000
            - 1 <= strs[i].length <= 1000
            - strs[i] all lowercase letters
        '''
        anagrams = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                count[idx] += 1
            
            anagrams[tuple(count)].append(s)

        return list(anagrams.values())

# Time complexity: O(n * m)
# Space complexity: O(n * m)