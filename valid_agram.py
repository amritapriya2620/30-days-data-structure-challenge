#Given two strings s and t, return true if t is an
#of s, and false otherwise.
#Example 1:
#Input: s = "anagram", t = "nagaram"
#Output: true
#Example 2:
#Input: s = "rat", t = "car"
#Output: false
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        if sorted(s)==sorted(t):
            return True
        else:
            return False
s=Solution()
print(s.isAnagram("anagram", "nagaram"))