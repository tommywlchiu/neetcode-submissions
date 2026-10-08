class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = {}

        if len(s) != len (t):
            return False

        for c in s:
            if c not in anagram:
                anagram[c] = 0
            anagram[c] += 1
        
        print(anagram)

        for c in t:
            if c not in anagram:
                return False
            anagram[c] -= 1
            if anagram[c] < 0:
                return False

        return True
