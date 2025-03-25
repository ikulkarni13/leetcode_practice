class Solution:
    def longestPalindromeChad(self, s: str) -> int:
        freaks = {}
        odd = 0
        longest = 0

        for char in s:
            if char in freaks:
                freaks[char] += 1
            else:
                freaks[char] = 1
        
        for freak in freaks.values():
            if freak % 2 == 0:
                longest += freak
            else:
                odd = 1
                longest += freak - 1

        return longest + odd
