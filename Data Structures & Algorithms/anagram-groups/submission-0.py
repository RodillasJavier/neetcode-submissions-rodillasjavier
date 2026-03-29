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
        anagrams = dict()

        for s in strs:
            key = "".join(sorted(s))

            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]

        res = []
        for key in anagrams:
            group = []
            for ana in anagrams[key]:
                group.append(ana)

            res.append(group)

        return res