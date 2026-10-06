class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #o(N) space
        #o(N) time??
        if len(nums) == 0:
            return 0
        hashset = set(nums)

        longest_seq = 0
        for n in nums:
            #check if it's a start of a seq
            
            if (n-1) not in hashset:
                #it is a start of a seq
                length = 0
                while (n+length) in hashset:
                    length += 1
                longest_seq = max(longest_seq,length)    

        return longest_seq
                    
                


            
        