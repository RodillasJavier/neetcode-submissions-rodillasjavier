from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = defaultdict(int)
        for num in nums:
            num_to_freq[num] += 1
        
        freq_to_num = defaultdict(list)
        max_freq = 0
        for num in num_to_freq:
            freq = num_to_freq[num]
            max_freq = max(max_freq, freq)

            freq_to_num[freq].append(num)
        
        i = max_freq
        res = []
        while len(res) < k:
            if i in freq_to_num:
                res.extend(freq_to_num[i])

            i -= 1
        
        return res[ : k]