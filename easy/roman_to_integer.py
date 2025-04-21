class Solution:
    def romanToIntChad(self, s: str) -> int:
        # create dict of roman numerals mapped to their values
        # iterate through the chars of inpt string

        # if the current roman numeral is the last one, add its value to the sum and return
        # if the current roman numeral is => the next one, add its value to the sum
        # else subtract its value from the sum

        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        total = 0

        for i, char in enumerate(s):
            if i == len(s) - 1:
                total += values[char]
            elif values[char] >= values[s[i+1]]:
                total += values[char]
            else:
                total -= values[char]

        return total
        