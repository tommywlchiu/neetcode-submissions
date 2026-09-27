class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #
        unique_num = {}
        res = []
        for num in nums:
            if num not in unique_num:
                unique_num[num] = 0
            unique_num[num] += 1
            # print(unique_num)

        sorted_freq = sorted(unique_num.items(), key=lambda x: x[1], reverse=True)
        # print(sorted_freq)

        for i in range(k):
            res.append(sorted_freq[i][0])
            # print(sorted_freq[i][0])

        return res