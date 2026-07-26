class Solution:
    def isPalindrome(self, s: str) -> bool:
        dup=""
        for c in s:
            if c.isalnum():
                dup+=c.lower()
        return dup==dup[::-1]
        
         