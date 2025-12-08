class Solution:
    def isPalindrome(self, s: str) -> bool:
        letter=""
        for ch in s:
            if ch.isalnum():
                letter +=ch.lower()
        return  letter == letter[::-1]
s=Solution()
print(s.isPalindrome( "A man, a plan, a canal: Panama"))