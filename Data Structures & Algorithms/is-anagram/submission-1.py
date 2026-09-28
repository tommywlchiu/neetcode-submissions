class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # if len(s) == len(t):
        #     if sorted(s) == sorted(t):
        #         return True   
        # return False
        if len(s) != len(t):
            return False

        char_count = {}


        for c in s:
            if c not in char_count:
                char_count[c] = 0
            char_count[c] += 1
        
        print(char_count)

        for c in t:
            if c not in char_count:
                return False
            char_count[c] -= 1
            if char_count[c] < 0:
                return False 
        return True
        