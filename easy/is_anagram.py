# sort both strings
# return true if they match
# otherwise return false

# iterate through t
# if any character doesn't occur in s the same number of times, return false
# otherwise return true

# s = 'a'
# t = 'aaa'

class Solution:
    def isAnagramChad(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        for char in set(s):
            if s.count(char) != t.count(char):
                return False
        
        return True