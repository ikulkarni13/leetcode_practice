class Solution:
    def containsDuplicate_chad(self, nums: List[int]) -> bool:
        # O(n) idea
        # iterate through the nums array, adding each value to a hash
        # if the value already exists within the hash, we found a duplicate and return true
        # once the entire search is complete, no duplicate has been found, return false

        seen = {}

        for num in nums:
            if num in seen:
                return True
            else:
                seen[num] = 1
        
        return False