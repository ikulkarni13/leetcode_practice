class Solution:
    def canConstructChad(self, ransomNote: str, magazine: str) -> bool:
        # ransom_note_set = set(ransomNote)

        # for char in ransom_note_set:
        #     if magazine.count(char) < ransomNote.count(char):
        #         return False
        
        # return True
        ransom_freq = {}
        mag_freq = {}

        for char in ransomNote:
            if char in ransom_freq:
                ransom_freq[char] += 1
            else:
                ransom_freq[char] = 1
        
        for char in magazine:
            if char in mag_freq:
                mag_freq[char] += 1
            else:
                mag_freq[char] = 1

        for char in set(ransomNote):
            if mag_freq.get(char, 0) < ransom_freq[char]:
                return False


        return True
