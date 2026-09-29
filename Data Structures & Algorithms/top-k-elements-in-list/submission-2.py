class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []

        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        # print(count)

        sorted_freq = sorted(count.items(), key = lambda x : x[1], reverse=True)
        # print(sorted_freq)
        for i in range(k):
            res.append(sorted_freq[i][0])
        return res