class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #o(N) space
        #o(N) time??
        
        if len(nums) == 0:
            return 0
        
        numSet = set(nums)
        longest = 0
        for n in nums:
            # print(n)
            if n-1 not in numSet:
                currSeq = 1
                while n + currSeq in numSet:
                    currSeq += 1
                longest = max(longest,currSeq)           
        return longest


            
        