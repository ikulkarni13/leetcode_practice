class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []

        for char in s:
            if char.isalnum():
                chars.append(char.lower())
                
        chars = ''.join(chars)
        return chars == chars[::-1]