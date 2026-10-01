class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []

        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
        
        sorted_freq = sorted(count.items(), key = lambda x : x[1], reverse=True)

        for i in range(k):
            res.append(sorted_freq[i][0])
        return res