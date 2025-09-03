class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if the length of strs if 1, return [strs[0]]
        # sort strs
        # iterate and

        anagrams = {}

        for string in strs:
            key = ''.join(sorted(string))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(string)

        return [array for array in anagrams.values()]