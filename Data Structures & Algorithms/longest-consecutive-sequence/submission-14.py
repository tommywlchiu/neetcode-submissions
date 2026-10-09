class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #o(N) space
        #o(N) time??
        
        if len(nums) == 0:
            return 0
        
        num_set = set(nums)
        print(num_set)
        longest = 0
        for n in nums:
            # check if this is the start of a seq
            # print(n-1)
            if (n-1) not in num_set:
                length = 1
                while n + length in num_set:
                    length += 1
                longest = max(longest,length)
        return longest
                


            
        